import json
import pprint
from linkml.utils.schema_builder import SchemaBuilder
from linkml_runtime.linkml_model import SchemaDefinition, ClassDefinition, SlotDefinition
from linkml_runtime.dumpers import yaml_dumper


def bioschemas_profile_to_linkml(jsonld_file: str):
    """
    Converts a Bioschemas.org based JSON-LD profile to its LinkML schema representation.
        @param: jsonld_file = local path to the Bioschema file
    """

    # Load Bioschemas JSON-LD profile
    with open(jsonld_file, 'r') as f:
        profile = json.load(f)
        ########################
        # Get profile metadata #
        ########################
        #
        #  Set license based on https://bioschemas.org/profiles/Dataset/1.0-RELEASE, as not in JSON-LD source
        bioschema_license = "https://creativecommons.org/licenses/by-sa/4.0/"
        #
        # get BioSchemas base url
        if "bioschemas" in profile["@context"]:
            base_url = profile["@context"]["bioschemas"]
        else:
            base_url = "https://discovery.biothings.io/view/bioschemas/"
        #
        # get profile name
        if 'rdfs:label' in profile["@graph"][0]:
            profile_name = profile["@graph"][0]['rdfs:label']
        elif "bioschemas:" in profile["@graph"][0]['@id']:
            profile_name = profile["@graph"][0]['@id'].split(':')[1]
        #
        # Instanciate linkML schema
        bioschemas_linkml = SchemaDefinition(name=profile_name.lower() + "_ap",
                                             title=f"Bioschemas.org's {profile_name} Profile LinkML representation",
                                             id=base_url + profile_name,
                                             description=profile["@graph"][0]["rdfs:comment"],
                                             version=profile["@graph"][0]["schema:schemaVersion"][0],
                                             license=bioschema_license,
                                             see_also=profile["@graph"][0]["schema:schemaVersion"][0],
                                             prefixes=profile["@context"],
                                             comments=["This LinkML representation of the Bioschemas Dataset "
                                                       "profile was automatically generated by parsing "
                                                       f"{profile["@graph"][0]["schema:schemaVersion"][0]}"]
                                             )
        schema_linkml = SchemaBuilder()
        schema_linkml.schema = bioschemas_linkml

        # Build profile main class
        schemaorg_superclass = profile["@graph"][0]["rdfs:subClassOf"]["@id"].split(":")[1]
        main_cls_slots = [slot for slot in profile["@graph"][0]["$validation"]["properties"]]
        schema_linkml.add_class(ClassDefinition(name=schemaorg_superclass,
                                                class_uri=profile["@graph"][0]["rdfs:subClassOf"]["@id"]))
        main_cls = ClassDefinition(name="Bioschemas" + profile_name,
                                   class_uri=profile["@graph"][0]["@id"],
                                   is_a=schemaorg_superclass,
                                   tree_root=True)

        main_cls.slots = main_cls_slots
        slot_usage = {}
        for slot in main_cls_slots:
            if slot in profile["@graph"][0]["$validation"]["required"]:
                slot_usage.update({slot: {"required": "true"}})
            elif slot in profile["@graph"][0]["$validation"]["recommended"]:
                slot_usage.update({slot: {"recommended": "true"}})
            elif slot in profile["@graph"][0]["$validation"]["optional"]:
                slot_usage.update({slot: {"comments": ["optional slot in Bioschemas profile"]}})
            schema_linkml.add_slot(SlotDefinition(name=slot,
                                                  slot_uri="schema:" + slot,
                                                  description=profile["@graph"][0]["$validation"]["properties"][slot][
                                                      "description"]))
        main_cls.slot_usage = slot_usage
        schema_linkml.add_class(main_cls)

        # Add classes used in profile slots as ranges
        classes = profile["@graph"][0]["$validation"]["definitions"]
        for cls in classes:
            # clean dirty JSON, by stripping inconsistent prefixes from @type field
            if ":" in classes[cls]["@type"]:
                classes[cls]["@type"] = classes[cls]["@type"].split(':')[1]
            for slot in classes[cls]["properties"]:
                if slot not in main_cls_slots:
                    schema_linkml.add_slot(SlotDefinition(name=slot,
                                                          slot_uri=f"schema:{slot}"))
            schema_linkml.add_class(ClassDefinition(name=classes[cls]['@type'],
                                                    slots=[slot for slot in classes[cls]["properties"]],
                                                    class_uri="schema:" + classes[cls]['@type']))

        schema_linkml.add_defaults()
        pprint.pprint(schema_linkml.as_dict())

        # Dump LinkML schema as YAML
        with open(f"dataset_ap/schema/dataset_ap.yaml", 'w') as stream:
            stream.write(yaml_dumper.dumps(schema_linkml.as_dict()))


# Example usage
bioschemas_profile_to_linkml("bioschema.jsonld")