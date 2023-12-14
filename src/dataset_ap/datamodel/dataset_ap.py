# Auto generated from dataset_ap.yaml by pythongen.py version: 0.0.1
# Generation date: 2023-12-14T23:14:13
# Schema: Dataset_AP
#
# id: https://w3id.org/storemphi/Dataset_AP
# description: A LinkML representation of https://bioschemas.org/profiles/Dataset/1.0-RELEASE.
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOSCHEMA = CurieNamespace('bioschema', 'https://bioschemas.org/properties/')
DATASET_AP = CurieNamespace('dataset_ap', 'https://w3id.org/storemphi/Dataset_AP/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCT = CurieNamespace('dct', 'purl.org/dc/terms/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
IAO = CurieNamespace('iao', 'http://purl.obolibrary.org/obo/IAO_/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OBI = CurieNamespace('obi', 'http://purl.obolibrary.org/obo/OBI_/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = DATASET_AP


# Types

# Class references
class ThingIdentifier(URIorCURIE):
    pass


class IntangibleIdentifier(ThingIdentifier):
    pass


class CreativeWorkIdentifier(ThingIdentifier):
    pass


class DatasetIdentifier(CreativeWorkIdentifier):
    pass


class DatasetCollectionIdentifier(CreativeWorkIdentifier):
    pass


class MaterialEntityIdentifier(ThingIdentifier):
    pass


class ChemicalEntityIdentifier(ThingIdentifier):
    pass


class EvaluatedThingIdentifier(ThingIdentifier):
    pass


class ChemicalReactionIdentifier(ThingIdentifier):
    pass


class ReactionStepIdentifier(ChemicalReactionIdentifier):
    pass


@dataclass
class Thing(YAMLRoot):
    """
    The most generic type of item.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.Thing

    identifier: Union[str, ThingIdentifier] = None
    alternateName: Optional[Union[str, List[str]]] = empty_list()
    description: Optional[str] = None
    name: Optional[str] = None
    sameAs: Optional[str] = None
    url: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, ThingIdentifier):
            self.identifier = ThingIdentifier(self.identifier)

        if not isinstance(self.alternateName, list):
            self.alternateName = [self.alternateName] if self.alternateName is not None else []
        self.alternateName = [v if isinstance(v, str) else str(v) for v in self.alternateName]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.sameAs is not None and not isinstance(self.sameAs, str):
            self.sameAs = str(self.sameAs)

        if self.url is not None and not isinstance(self.url, URIorCURIE):
            self.url = URIorCURIE(self.url)

        super().__post_init__(**kwargs)


@dataclass
class Intangible(Thing):
    """
    A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured
    values, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Intangible"]
    class_class_curie: ClassVar[str] = "schema:Intangible"
    class_name: ClassVar[str] = "Intangible"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.Intangible

    identifier: Union[str, IntangibleIdentifier] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, IntangibleIdentifier):
            self.identifier = IntangibleIdentifier(self.identifier)

        super().__post_init__(**kwargs)


@dataclass
class CreativeWork(Thing):
    """
    The most generic kind of creative work, including books, movies, photographs, software programs, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["CreativeWork"]
    class_class_curie: ClassVar[str] = "schema:CreativeWork"
    class_name: ClassVar[str] = "CreativeWork"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.CreativeWork

    identifier: Union[str, CreativeWorkIdentifier] = None
    citation: Optional[str] = None
    creator: Optional[str] = None
    dateCreated: Optional[str] = None
    dateModified: Optional[str] = None
    datePublished: Optional[str] = None
    hasPart: Optional[str] = None
    isAccessibleForFree: Optional[str] = None
    isBasedOn: Optional[str] = None
    isPartOf: Optional[str] = None
    keywords: Optional[str] = None
    license: Optional[str] = None
    maintainer: Optional[str] = None
    publisher: Optional[str] = None
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, CreativeWorkIdentifier):
            self.identifier = CreativeWorkIdentifier(self.identifier)

        if self.citation is not None and not isinstance(self.citation, str):
            self.citation = str(self.citation)

        if self.creator is not None and not isinstance(self.creator, str):
            self.creator = str(self.creator)

        if self.dateCreated is not None and not isinstance(self.dateCreated, str):
            self.dateCreated = str(self.dateCreated)

        if self.dateModified is not None and not isinstance(self.dateModified, str):
            self.dateModified = str(self.dateModified)

        if self.datePublished is not None and not isinstance(self.datePublished, str):
            self.datePublished = str(self.datePublished)

        if self.hasPart is not None and not isinstance(self.hasPart, str):
            self.hasPart = str(self.hasPart)

        if self.isAccessibleForFree is not None and not isinstance(self.isAccessibleForFree, str):
            self.isAccessibleForFree = str(self.isAccessibleForFree)

        if self.isBasedOn is not None and not isinstance(self.isBasedOn, str):
            self.isBasedOn = str(self.isBasedOn)

        if self.isPartOf is not None and not isinstance(self.isPartOf, str):
            self.isPartOf = str(self.isPartOf)

        if self.keywords is not None and not isinstance(self.keywords, str):
            self.keywords = str(self.keywords)

        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.maintainer is not None and not isinstance(self.maintainer, str):
            self.maintainer = str(self.maintainer)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass
class Dataset(CreativeWork):
    """
    Represents a Dataset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Dataset"]
    class_class_curie: ClassVar[str] = "schema:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.Dataset

    identifier: Union[str, DatasetIdentifier] = None
    conformsTo: str = None
    description: str = None
    keywords: str = None
    license: str = None
    name: str = None
    url: Union[str, URIorCURIE] = None
    distribution: Optional[str] = None
    includedInDataCatalog: Optional[Union[str, DatasetCollectionIdentifier]] = None
    issn: Optional[str] = None
    measurementMethod: Optional[str] = None
    measurementTechnique: Optional[str] = None
    variableMeasured: Optional[str] = None
    alternateName: Optional[Union[str, List[str]]] = empty_list()
    citation: Optional[str] = None
    creator: Optional[str] = None
    datePublished: Optional[str] = None
    isBasedOn: Optional[str] = None
    publisher: Optional[str] = None
    version: Optional[str] = None
    dateCreated: Optional[str] = None
    dateModified: Optional[str] = None
    hasPart: Optional[str] = None
    isPartOf: Optional[str] = None
    isAccessibleForFree: Optional[str] = None
    maintainer: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, DatasetIdentifier):
            self.identifier = DatasetIdentifier(self.identifier)

        if self._is_empty(self.conformsTo):
            self.MissingRequiredField("conformsTo")
        if not isinstance(self.conformsTo, str):
            self.conformsTo = str(self.conformsTo)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.keywords):
            self.MissingRequiredField("keywords")
        if not isinstance(self.keywords, str):
            self.keywords = str(self.keywords)

        if self._is_empty(self.license):
            self.MissingRequiredField("license")
        if not isinstance(self.license, str):
            self.license = str(self.license)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, URIorCURIE):
            self.url = URIorCURIE(self.url)

        if self.distribution is not None and not isinstance(self.distribution, str):
            self.distribution = str(self.distribution)

        if self.includedInDataCatalog is not None and not isinstance(self.includedInDataCatalog, DatasetCollectionIdentifier):
            self.includedInDataCatalog = DatasetCollectionIdentifier(self.includedInDataCatalog)

        if self.issn is not None and not isinstance(self.issn, str):
            self.issn = str(self.issn)

        if self.measurementMethod is not None and not isinstance(self.measurementMethod, str):
            self.measurementMethod = str(self.measurementMethod)

        if self.measurementTechnique is not None and not isinstance(self.measurementTechnique, str):
            self.measurementTechnique = str(self.measurementTechnique)

        if self.variableMeasured is not None and not isinstance(self.variableMeasured, str):
            self.variableMeasured = str(self.variableMeasured)

        if not isinstance(self.alternateName, list):
            self.alternateName = [self.alternateName] if self.alternateName is not None else []
        self.alternateName = [v if isinstance(v, str) else str(v) for v in self.alternateName]

        if self.citation is not None and not isinstance(self.citation, str):
            self.citation = str(self.citation)

        if self.creator is not None and not isinstance(self.creator, str):
            self.creator = str(self.creator)

        if self.datePublished is not None and not isinstance(self.datePublished, str):
            self.datePublished = str(self.datePublished)

        if self.isBasedOn is not None and not isinstance(self.isBasedOn, str):
            self.isBasedOn = str(self.isBasedOn)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.dateCreated is not None and not isinstance(self.dateCreated, str):
            self.dateCreated = str(self.dateCreated)

        if self.dateModified is not None and not isinstance(self.dateModified, str):
            self.dateModified = str(self.dateModified)

        if self.hasPart is not None and not isinstance(self.hasPart, str):
            self.hasPart = str(self.hasPart)

        if self.isPartOf is not None and not isinstance(self.isPartOf, str):
            self.isPartOf = str(self.isPartOf)

        if self.isAccessibleForFree is not None and not isinstance(self.isAccessibleForFree, str):
            self.isAccessibleForFree = str(self.isAccessibleForFree)

        if self.maintainer is not None and not isinstance(self.maintainer, str):
            self.maintainer = str(self.maintainer)

        super().__post_init__(**kwargs)


@dataclass
class DatasetCollection(CreativeWork):
    """
    A collection of datasets.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["DataCatalog"]
    class_class_curie: ClassVar[str] = "schema:DataCatalog"
    class_name: ClassVar[str] = "DatasetCollection"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.DatasetCollection

    identifier: Union[str, DatasetCollectionIdentifier] = None
    datasets: Union[Dict[Union[str, DatasetIdentifier], Union[dict, Dataset]], List[Union[dict, Dataset]]] = empty_dict()
    measurementMethod: Optional[str] = None
    measurementTechnique: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, DatasetCollectionIdentifier):
            self.identifier = DatasetCollectionIdentifier(self.identifier)

        if self._is_empty(self.datasets):
            self.MissingRequiredField("datasets")
        self._normalize_inlined_as_dict(slot_name="datasets", slot_type=Dataset, key_name="identifier", keyed=True)

        if self.measurementMethod is not None and not isinstance(self.measurementMethod, str):
            self.measurementMethod = str(self.measurementMethod)

        if self.measurementTechnique is not None and not isinstance(self.measurementTechnique, str):
            self.measurementTechnique = str(self.measurementTechnique)

        super().__post_init__(**kwargs)


@dataclass
class MaterialEntity(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DATASET_AP["MaterialEntity"]
    class_class_curie: ClassVar[str] = "dataset_ap:MaterialEntity"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.MaterialEntity

    identifier: Union[str, MaterialEntityIdentifier] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, MaterialEntityIdentifier):
            self.identifier = MaterialEntityIdentifier(self.identifier)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalEntity(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DATASET_AP["ChemicalEntity"]
    class_class_curie: ClassVar[str] = "dataset_ap:ChemicalEntity"
    class_name: ClassVar[str] = "ChemicalEntity"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.ChemicalEntity

    identifier: Union[str, ChemicalEntityIdentifier] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, ChemicalEntityIdentifier):
            self.identifier = ChemicalEntityIdentifier(self.identifier)

        super().__post_init__(**kwargs)


@dataclass
class EvaluatedThing(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DATASET_AP["EvaluatedThing"]
    class_class_curie: ClassVar[str] = "dataset_ap:EvaluatedThing"
    class_name: ClassVar[str] = "EvaluatedThing"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.EvaluatedThing

    identifier: Union[str, EvaluatedThingIdentifier] = None

@dataclass
class ChemicalReaction(Thing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DATASET_AP["ChemicalReaction"]
    class_class_curie: ClassVar[str] = "dataset_ap:ChemicalReaction"
    class_name: ClassVar[str] = "ChemicalReaction"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.ChemicalReaction

    identifier: Union[str, ChemicalReactionIdentifier] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, ChemicalReactionIdentifier):
            self.identifier = ChemicalReactionIdentifier(self.identifier)

        super().__post_init__(**kwargs)


@dataclass
class ReactionStep(ChemicalReaction):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DATASET_AP["ReactionStep"]
    class_class_curie: ClassVar[str] = "dataset_ap:ReactionStep"
    class_name: ClassVar[str] = "ReactionStep"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.ReactionStep

    identifier: Union[str, ReactionStepIdentifier] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, ReactionStepIdentifier):
            self.identifier = ReactionStepIdentifier(self.identifier)

        super().__post_init__(**kwargs)


class PlannedProcess(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000011"]
    class_class_curie: ClassVar[str] = "obi:0000011"
    class_name: ClassVar[str] = "PlannedProcess"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.PlannedProcess


@dataclass
class Assay(PlannedProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000070"]
    class_class_curie: ClassVar[str] = "obi:0000070"
    class_name: ClassVar[str] = "Assay"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.Assay

    has_input: Optional[Union[str, EvaluatedThingIdentifier]] = None
    has_output: Optional[Union[str, DatasetIdentifier]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.has_input is not None and not isinstance(self.has_input, EvaluatedThingIdentifier):
            self.has_input = EvaluatedThingIdentifier(self.has_input)

        if self.has_output is not None and not isinstance(self.has_output, DatasetIdentifier):
            self.has_output = DatasetIdentifier(self.has_output)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.identifier = Slot(uri=SCHEMA.identifier, name="identifier", curie=SCHEMA.curie('identifier'),
                   model_uri=DATASET_AP.identifier, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=DATASET_AP.name, domain=None, range=Optional[str])

slots.alternateName = Slot(uri=SCHEMA.alternateName, name="alternateName", curie=SCHEMA.curie('alternateName'),
                   model_uri=DATASET_AP.alternateName, domain=None, range=Optional[Union[str, List[str]]])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=DATASET_AP.description, domain=None, range=Optional[str])

slots.sameAs = Slot(uri=SCHEMA.sameAs, name="sameAs", curie=SCHEMA.curie('sameAs'),
                   model_uri=DATASET_AP.sameAs, domain=None, range=Optional[str])

slots.url = Slot(uri=SCHEMA.url, name="url", curie=SCHEMA.curie('url'),
                   model_uri=DATASET_AP.url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.subjectOf = Slot(uri=SCHEMA.subjectOf, name="subjectOf", curie=SCHEMA.curie('subjectOf'),
                   model_uri=DATASET_AP.subjectOf, domain=Thing, range=Optional[Union[str, CreativeWorkIdentifier]])

slots.about = Slot(uri=SCHEMA.about, name="about", curie=SCHEMA.curie('about'),
                   model_uri=DATASET_AP.about, domain=CreativeWork, range=Optional[Union[str, ThingIdentifier]])

slots.citation = Slot(uri=DATASET_AP.citation, name="citation", curie=DATASET_AP.curie('citation'),
                   model_uri=DATASET_AP.citation, domain=None, range=Optional[str])

slots.creator = Slot(uri=SCHEMA.creator, name="creator", curie=SCHEMA.curie('creator'),
                   model_uri=DATASET_AP.creator, domain=None, range=Optional[str])

slots.dateCreated = Slot(uri=SCHEMA.dateCreated, name="dateCreated", curie=SCHEMA.curie('dateCreated'),
                   model_uri=DATASET_AP.dateCreated, domain=None, range=Optional[str])

slots.dateModified = Slot(uri=DATASET_AP.dateModified, name="dateModified", curie=DATASET_AP.curie('dateModified'),
                   model_uri=DATASET_AP.dateModified, domain=None, range=Optional[str])

slots.datePublished = Slot(uri=DATASET_AP.datePublished, name="datePublished", curie=DATASET_AP.curie('datePublished'),
                   model_uri=DATASET_AP.datePublished, domain=None, range=Optional[str])

slots.hasPart = Slot(uri=DATASET_AP.hasPart, name="hasPart", curie=DATASET_AP.curie('hasPart'),
                   model_uri=DATASET_AP.hasPart, domain=None, range=Optional[str])

slots.isAccessibleForFree = Slot(uri=DATASET_AP.isAccessibleForFree, name="isAccessibleForFree", curie=DATASET_AP.curie('isAccessibleForFree'),
                   model_uri=DATASET_AP.isAccessibleForFree, domain=None, range=Optional[str])

slots.isBasedOn = Slot(uri=SCHEMA.isBasedOn, name="isBasedOn", curie=SCHEMA.curie('isBasedOn'),
                   model_uri=DATASET_AP.isBasedOn, domain=None, range=Optional[str])

slots.isPartOf = Slot(uri=DATASET_AP.isPartOf, name="isPartOf", curie=DATASET_AP.curie('isPartOf'),
                   model_uri=DATASET_AP.isPartOf, domain=None, range=Optional[str])

slots.keywords = Slot(uri=DATASET_AP.keywords, name="keywords", curie=DATASET_AP.curie('keywords'),
                   model_uri=DATASET_AP.keywords, domain=None, range=Optional[str])

slots.license = Slot(uri=DATASET_AP.license, name="license", curie=DATASET_AP.curie('license'),
                   model_uri=DATASET_AP.license, domain=None, range=Optional[str])

slots.maintainer = Slot(uri=DATASET_AP.maintainer, name="maintainer", curie=DATASET_AP.curie('maintainer'),
                   model_uri=DATASET_AP.maintainer, domain=None, range=Optional[str])

slots.publisher = Slot(uri=DATASET_AP.publisher, name="publisher", curie=DATASET_AP.curie('publisher'),
                   model_uri=DATASET_AP.publisher, domain=None, range=Optional[str])

slots.version = Slot(uri=DATASET_AP.version, name="version", curie=DATASET_AP.curie('version'),
                   model_uri=DATASET_AP.version, domain=None, range=Optional[str])

slots.distribution = Slot(uri=SCHEMA.distribution, name="distribution", curie=SCHEMA.curie('distribution'),
                   model_uri=DATASET_AP.distribution, domain=None, range=Optional[str])

slots.includedInDataCatalog = Slot(uri=SCHEMA.includedInDataCatalog, name="includedInDataCatalog", curie=SCHEMA.curie('includedInDataCatalog'),
                   model_uri=DATASET_AP.includedInDataCatalog, domain=None, range=Optional[Union[str, DatasetCollectionIdentifier]])

slots.issn = Slot(uri=SCHEMA.issn, name="issn", curie=SCHEMA.curie('issn'),
                   model_uri=DATASET_AP.issn, domain=None, range=Optional[str])

slots.measurementMethod = Slot(uri=SCHEMA.measurementMethod, name="measurementMethod", curie=SCHEMA.curie('measurementMethod'),
                   model_uri=DATASET_AP.measurementMethod, domain=None, range=Optional[str])

slots.measurementTechnique = Slot(uri=SCHEMA.measurementTechnique, name="measurementTechnique", curie=SCHEMA.curie('measurementTechnique'),
                   model_uri=DATASET_AP.measurementTechnique, domain=None, range=Optional[str])

slots.variableMeasured = Slot(uri=SCHEMA.variableMeasured, name="variableMeasured", curie=SCHEMA.curie('variableMeasured'),
                   model_uri=DATASET_AP.variableMeasured, domain=None, range=Optional[str])

slots.conformsTo = Slot(uri=DCT.conformsTo, name="conformsTo", curie=DCT.curie('conformsTo'),
                   model_uri=DATASET_AP.conformsTo, domain=None, range=str)

slots.datasets = Slot(uri=SCHEMA.dataset, name="datasets", curie=SCHEMA.curie('dataset'),
                   model_uri=DATASET_AP.datasets, domain=None, range=Union[Dict[Union[str, DatasetIdentifier], Union[dict, Dataset]], List[Union[dict, Dataset]]])

slots.has_input = Slot(uri=DATASET_AP.has_input, name="has_input", curie=DATASET_AP.curie('has_input'),
                   model_uri=DATASET_AP.has_input, domain=Assay, range=Optional[Union[str, EvaluatedThingIdentifier]])

slots.has_output = Slot(uri=DATASET_AP.has_output, name="has_output", curie=DATASET_AP.curie('has_output'),
                   model_uri=DATASET_AP.has_output, domain=Assay, range=Optional[Union[str, DatasetIdentifier]])

slots.has_parameter = Slot(uri=DATASET_AP.has_parameter, name="has_parameter", curie=DATASET_AP.curie('has_parameter'),
                   model_uri=DATASET_AP.has_parameter, domain=Assay, range=Optional[str])

slots.Dataset_conformsTo = Slot(uri=DCT.conformsTo, name="Dataset_conformsTo", curie=DCT.curie('conformsTo'),
                   model_uri=DATASET_AP.Dataset_conformsTo, domain=Dataset, range=str)

slots.Dataset_description = Slot(uri=SCHEMA.description, name="Dataset_description", curie=SCHEMA.curie('description'),
                   model_uri=DATASET_AP.Dataset_description, domain=Dataset, range=str)

slots.Dataset_keywords = Slot(uri=DATASET_AP.keywords, name="Dataset_keywords", curie=DATASET_AP.curie('keywords'),
                   model_uri=DATASET_AP.Dataset_keywords, domain=Dataset, range=str)

slots.Dataset_license = Slot(uri=DATASET_AP.license, name="Dataset_license", curie=DATASET_AP.curie('license'),
                   model_uri=DATASET_AP.Dataset_license, domain=Dataset, range=str)

slots.Dataset_name = Slot(uri=SCHEMA.name, name="Dataset_name", curie=SCHEMA.curie('name'),
                   model_uri=DATASET_AP.Dataset_name, domain=Dataset, range=str)

slots.Dataset_url = Slot(uri=SCHEMA.url, name="Dataset_url", curie=SCHEMA.curie('url'),
                   model_uri=DATASET_AP.Dataset_url, domain=Dataset, range=Union[str, URIorCURIE])

slots.Dataset_alternateName = Slot(uri=SCHEMA.alternateName, name="Dataset_alternateName", curie=SCHEMA.curie('alternateName'),
                   model_uri=DATASET_AP.Dataset_alternateName, domain=Dataset, range=Optional[Union[str, List[str]]])

slots.Dataset_citation = Slot(uri=DATASET_AP.citation, name="Dataset_citation", curie=DATASET_AP.curie('citation'),
                   model_uri=DATASET_AP.Dataset_citation, domain=Dataset, range=Optional[str])

slots.Dataset_creator = Slot(uri=SCHEMA.creator, name="Dataset_creator", curie=SCHEMA.curie('creator'),
                   model_uri=DATASET_AP.Dataset_creator, domain=Dataset, range=Optional[str])

slots.Dataset_datePublished = Slot(uri=DATASET_AP.datePublished, name="Dataset_datePublished", curie=DATASET_AP.curie('datePublished'),
                   model_uri=DATASET_AP.Dataset_datePublished, domain=Dataset, range=Optional[str])

slots.Dataset_distribution = Slot(uri=SCHEMA.distribution, name="Dataset_distribution", curie=SCHEMA.curie('distribution'),
                   model_uri=DATASET_AP.Dataset_distribution, domain=Dataset, range=Optional[str])

slots.Dataset_includedInDataCatalog = Slot(uri=SCHEMA.includedInDataCatalog, name="Dataset_includedInDataCatalog", curie=SCHEMA.curie('includedInDataCatalog'),
                   model_uri=DATASET_AP.Dataset_includedInDataCatalog, domain=Dataset, range=Optional[Union[str, DatasetCollectionIdentifier]])

slots.Dataset_isBasedOn = Slot(uri=SCHEMA.isBasedOn, name="Dataset_isBasedOn", curie=SCHEMA.curie('isBasedOn'),
                   model_uri=DATASET_AP.Dataset_isBasedOn, domain=Dataset, range=Optional[str])

slots.Dataset_measurementTechnique = Slot(uri=SCHEMA.measurementTechnique, name="Dataset_measurementTechnique", curie=SCHEMA.curie('measurementTechnique'),
                   model_uri=DATASET_AP.Dataset_measurementTechnique, domain=Dataset, range=Optional[str])

slots.Dataset_publisher = Slot(uri=DATASET_AP.publisher, name="Dataset_publisher", curie=DATASET_AP.curie('publisher'),
                   model_uri=DATASET_AP.Dataset_publisher, domain=Dataset, range=Optional[str])

slots.Dataset_variableMeasured = Slot(uri=SCHEMA.variableMeasured, name="Dataset_variableMeasured", curie=SCHEMA.curie('variableMeasured'),
                   model_uri=DATASET_AP.Dataset_variableMeasured, domain=Dataset, range=Optional[str])

slots.Dataset_version = Slot(uri=DATASET_AP.version, name="Dataset_version", curie=DATASET_AP.curie('version'),
                   model_uri=DATASET_AP.Dataset_version, domain=Dataset, range=Optional[str])

slots.Dataset_dateCreated = Slot(uri=SCHEMA.dateCreated, name="Dataset_dateCreated", curie=SCHEMA.curie('dateCreated'),
                   model_uri=DATASET_AP.Dataset_dateCreated, domain=Dataset, range=Optional[str])

slots.Dataset_dateModified = Slot(uri=DATASET_AP.dateModified, name="Dataset_dateModified", curie=DATASET_AP.curie('dateModified'),
                   model_uri=DATASET_AP.Dataset_dateModified, domain=Dataset, range=Optional[str])

slots.Dataset_hasPart = Slot(uri=DATASET_AP.hasPart, name="Dataset_hasPart", curie=DATASET_AP.curie('hasPart'),
                   model_uri=DATASET_AP.Dataset_hasPart, domain=Dataset, range=Optional[str])

slots.Dataset_isPartOf = Slot(uri=DATASET_AP.isPartOf, name="Dataset_isPartOf", curie=DATASET_AP.curie('isPartOf'),
                   model_uri=DATASET_AP.Dataset_isPartOf, domain=Dataset, range=Optional[str])

slots.Dataset_isAccessibleForFree = Slot(uri=DATASET_AP.isAccessibleForFree, name="Dataset_isAccessibleForFree", curie=DATASET_AP.curie('isAccessibleForFree'),
                   model_uri=DATASET_AP.Dataset_isAccessibleForFree, domain=Dataset, range=Optional[str])

slots.Dataset_maintainer = Slot(uri=DATASET_AP.maintainer, name="Dataset_maintainer", curie=DATASET_AP.curie('maintainer'),
                   model_uri=DATASET_AP.Dataset_maintainer, domain=Dataset, range=Optional[str])