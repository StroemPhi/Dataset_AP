# Auto generated from dataset_ap.yaml by pythongen.py version: 0.0.1
# Generation date: 2023-12-17T23:36:53
# Schema: dataset_ap
#
# id: https://discovery.biothings.io/view/bioschemas/Dataset
# description: A guide for how to describe datasets in the life-sciences using Schema.org-like annotation. Version 1.0-RELEASE. <h3>Summary of Changes</h3> <br>Key changes since 0.3-RELEASE:<ul><li>Updated properties to Schema.org v12.0; various properties added at recommended or optional level, expected types updated. See 0.4-DRAFT for full details</li><li>license now a minimum property</li><li>keywords: Cardinality #501 – Cardinality is MANY</li><li>distribution: Cardinality #574 – Cardinality changed to MANY</li><li>datePublished: Increased marginlity #576 – Now recommended</li><li>publisher: Increased marginlity, Cardinality #576 – Now recommended with MANY cardinality</li></ul>
# license: https://creativecommons.org/licenses/by-sa/4.0/

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
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = "https://bioschemas.org/profiles/Dataset/1.0-RELEASE"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOSCHEMAS = CurieNamespace('bioschemas', 'https://discovery.biothings.io/view/bioschemas/')
DATASET_AP = CurieNamespace('dataset_ap', 'https://discovery.biothings.io/view/bioschemas/Dataset/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = DATASET_AP


# Types

# Class references



class Dataset(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Dataset"]
    class_class_curie: ClassVar[str] = "schema:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.Dataset


@dataclass
class BioschemasDataset(Dataset):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOSCHEMAS["Dataset"]
    class_class_curie: ClassVar[str] = "bioschemas:Dataset"
    class_name: ClassVar[str] = "BioschemasDataset"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.BioschemasDataset

    description: str = None
    identifier: str = None
    keywords: str = None
    license: str = None
    name: str = None
    url: str = None
    alternateName: Optional[str] = None
    citation: Optional[str] = None
    creator: Optional[str] = None
    dateCreated: Optional[str] = None
    dateModified: Optional[str] = None
    datePublished: Optional[str] = None
    distribution: Optional[str] = None
    hasPart: Optional[str] = None
    includedInDataCatalog: Optional[str] = None
    isAccessibleForFree: Optional[str] = None
    isBasedOn: Optional[str] = None
    isPartOf: Optional[str] = None
    maintainer: Optional[str] = None
    measurementTechnique: Optional[str] = None
    publisher: Optional[str] = None
    sameAs: Optional[str] = None
    variableMeasured: Optional[str] = None
    version: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

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
        if not isinstance(self.url, str):
            self.url = str(self.url)

        if self.alternateName is not None and not isinstance(self.alternateName, str):
            self.alternateName = str(self.alternateName)

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

        if self.distribution is not None and not isinstance(self.distribution, str):
            self.distribution = str(self.distribution)

        if self.hasPart is not None and not isinstance(self.hasPart, str):
            self.hasPart = str(self.hasPart)

        if self.includedInDataCatalog is not None and not isinstance(self.includedInDataCatalog, str):
            self.includedInDataCatalog = str(self.includedInDataCatalog)

        if self.isAccessibleForFree is not None and not isinstance(self.isAccessibleForFree, str):
            self.isAccessibleForFree = str(self.isAccessibleForFree)

        if self.isBasedOn is not None and not isinstance(self.isBasedOn, str):
            self.isBasedOn = str(self.isBasedOn)

        if self.isPartOf is not None and not isinstance(self.isPartOf, str):
            self.isPartOf = str(self.isPartOf)

        if self.maintainer is not None and not isinstance(self.maintainer, str):
            self.maintainer = str(self.maintainer)

        if self.measurementTechnique is not None and not isinstance(self.measurementTechnique, str):
            self.measurementTechnique = str(self.measurementTechnique)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.sameAs is not None and not isinstance(self.sameAs, str):
            self.sameAs = str(self.sameAs)

        if self.variableMeasured is not None and not isinstance(self.variableMeasured, str):
            self.variableMeasured = str(self.variableMeasured)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass
class CreativeWork(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["CreativeWork"]
    class_class_curie: ClassVar[str] = "schema:CreativeWork"
    class_name: ClassVar[str] = "CreativeWork"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.CreativeWork

    name: Optional[str] = None
    identifier: Optional[str] = None
    url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


@dataclass
class Organization(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Organization"]
    class_class_curie: ClassVar[str] = "schema:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.Organization

    name: Optional[str] = None
    legalName: Optional[str] = None
    description: Optional[str] = None
    sameAs: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.legalName is not None and not isinstance(self.legalName, str):
            self.legalName = str(self.legalName)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.sameAs is not None and not isinstance(self.sameAs, str):
            self.sameAs = str(self.sameAs)

        super().__post_init__(**kwargs)


@dataclass
class Person(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Person"]
    class_class_curie: ClassVar[str] = "schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.Person

    name: Optional[str] = None
    url: Optional[str] = None
    mainEntityOfPage: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.mainEntityOfPage is not None and not isinstance(self.mainEntityOfPage, str):
            self.mainEntityOfPage = str(self.mainEntityOfPage)

        super().__post_init__(**kwargs)


@dataclass
class DateTime(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["DateTime"]
    class_class_curie: ClassVar[str] = "schema:DateTime"
    class_name: ClassVar[str] = "DateTime"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.DateTime

    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class DataDownload(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["DataDownload"]
    class_class_curie: ClassVar[str] = "schema:DataDownload"
    class_name: ClassVar[str] = "DataDownload"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.DataDownload

    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Trip(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Trip"]
    class_class_curie: ClassVar[str] = "schema:Trip"
    class_name: ClassVar[str] = "Trip"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.Trip

    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class PropertyValue(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["PropertyValue"]
    class_class_curie: ClassVar[str] = "schema:PropertyValue"
    class_name: ClassVar[str] = "PropertyValue"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.PropertyValue

    name: Optional[str] = None
    value: Optional[str] = None
    identifier: Optional[str] = None
    valuereference: Optional[str] = None
    unitCode: Optional[str] = None
    unitText: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.valuereference is not None and not isinstance(self.valuereference, str):
            self.valuereference = str(self.valuereference)

        if self.unitCode is not None and not isinstance(self.unitCode, str):
            self.unitCode = str(self.unitCode)

        if self.unitText is not None and not isinstance(self.unitText, str):
            self.unitText = str(self.unitText)

        super().__post_init__(**kwargs)


@dataclass
class CategoryCode(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["CategoryCode"]
    class_class_curie: ClassVar[str] = "schema:CategoryCode"
    class_name: ClassVar[str] = "CategoryCode"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.CategoryCode

    name: Optional[str] = None
    codeValue: Optional[str] = None
    url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.codeValue is not None and not isinstance(self.codeValue, str):
            self.codeValue = str(self.codeValue)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


@dataclass
class DataCatalog(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["DataCatalog"]
    class_class_curie: ClassVar[str] = "schema:DataCatalog"
    class_name: ClassVar[str] = "DataCatalog"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.DataCatalog

    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Product(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Product"]
    class_class_curie: ClassVar[str] = "schema:Product"
    class_name: ClassVar[str] = "Product"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.Product

    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class DefinedTerm(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["DefinedTerm"]
    class_class_curie: ClassVar[str] = "schema:DefinedTerm"
    class_name: ClassVar[str] = "DefinedTerm"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.DefinedTerm

    url: Optional[str] = None
    name: Optional[str] = None
    termCode: Optional[str] = None
    identifier: Optional[str] = None
    inDefinedTermSet: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.termCode is not None and not isinstance(self.termCode, str):
            self.termCode = str(self.termCode)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.inDefinedTermSet is not None and not isinstance(self.inDefinedTermSet, str):
            self.inDefinedTermSet = str(self.inDefinedTermSet)

        super().__post_init__(**kwargs)


@dataclass
class DefinedTermSet(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["DefinedTermSet"]
    class_class_curie: ClassVar[str] = "schema:DefinedTermSet"
    class_name: ClassVar[str] = "DefinedTermSet"
    class_model_uri: ClassVar[URIRef] = DATASET_AP.DefinedTermSet

    name: Optional[str] = None
    identifier: Optional[str] = None
    url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.alternateName = Slot(uri=SCHEMA.alternateName, name="alternateName", curie=SCHEMA.curie('alternateName'),
                   model_uri=DATASET_AP.alternateName, domain=None, range=Optional[str])

slots.citation = Slot(uri=SCHEMA.citation, name="citation", curie=SCHEMA.curie('citation'),
                   model_uri=DATASET_AP.citation, domain=None, range=Optional[str])

slots.creator = Slot(uri=SCHEMA.creator, name="creator", curie=SCHEMA.curie('creator'),
                   model_uri=DATASET_AP.creator, domain=None, range=Optional[str])

slots.dateCreated = Slot(uri=SCHEMA.dateCreated, name="dateCreated", curie=SCHEMA.curie('dateCreated'),
                   model_uri=DATASET_AP.dateCreated, domain=None, range=Optional[str])

slots.dateModified = Slot(uri=SCHEMA.dateModified, name="dateModified", curie=SCHEMA.curie('dateModified'),
                   model_uri=DATASET_AP.dateModified, domain=None, range=Optional[str])

slots.datePublished = Slot(uri=SCHEMA.datePublished, name="datePublished", curie=SCHEMA.curie('datePublished'),
                   model_uri=DATASET_AP.datePublished, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=DATASET_AP.description, domain=None, range=Optional[str])

slots.distribution = Slot(uri=SCHEMA.distribution, name="distribution", curie=SCHEMA.curie('distribution'),
                   model_uri=DATASET_AP.distribution, domain=None, range=Optional[str])

slots.hasPart = Slot(uri=SCHEMA.hasPart, name="hasPart", curie=SCHEMA.curie('hasPart'),
                   model_uri=DATASET_AP.hasPart, domain=None, range=Optional[str])

slots.identifier = Slot(uri=SCHEMA.identifier, name="identifier", curie=SCHEMA.curie('identifier'),
                   model_uri=DATASET_AP.identifier, domain=None, range=Optional[str])

slots.includedInDataCatalog = Slot(uri=SCHEMA.includedInDataCatalog, name="includedInDataCatalog", curie=SCHEMA.curie('includedInDataCatalog'),
                   model_uri=DATASET_AP.includedInDataCatalog, domain=None, range=Optional[str])

slots.isAccessibleForFree = Slot(uri=SCHEMA.isAccessibleForFree, name="isAccessibleForFree", curie=SCHEMA.curie('isAccessibleForFree'),
                   model_uri=DATASET_AP.isAccessibleForFree, domain=None, range=Optional[str])

slots.isBasedOn = Slot(uri=SCHEMA.isBasedOn, name="isBasedOn", curie=SCHEMA.curie('isBasedOn'),
                   model_uri=DATASET_AP.isBasedOn, domain=None, range=Optional[str])

slots.isPartOf = Slot(uri=SCHEMA.isPartOf, name="isPartOf", curie=SCHEMA.curie('isPartOf'),
                   model_uri=DATASET_AP.isPartOf, domain=None, range=Optional[str])

slots.keywords = Slot(uri=SCHEMA.keywords, name="keywords", curie=SCHEMA.curie('keywords'),
                   model_uri=DATASET_AP.keywords, domain=None, range=Optional[str])

slots.license = Slot(uri=SCHEMA.license, name="license", curie=SCHEMA.curie('license'),
                   model_uri=DATASET_AP.license, domain=None, range=Optional[str])

slots.maintainer = Slot(uri=SCHEMA.maintainer, name="maintainer", curie=SCHEMA.curie('maintainer'),
                   model_uri=DATASET_AP.maintainer, domain=None, range=Optional[str])

slots.measurementTechnique = Slot(uri=SCHEMA.measurementTechnique, name="measurementTechnique", curie=SCHEMA.curie('measurementTechnique'),
                   model_uri=DATASET_AP.measurementTechnique, domain=None, range=Optional[str])

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=DATASET_AP.name, domain=None, range=Optional[str])

slots.publisher = Slot(uri=SCHEMA.publisher, name="publisher", curie=SCHEMA.curie('publisher'),
                   model_uri=DATASET_AP.publisher, domain=None, range=Optional[str])

slots.sameAs = Slot(uri=SCHEMA.sameAs, name="sameAs", curie=SCHEMA.curie('sameAs'),
                   model_uri=DATASET_AP.sameAs, domain=None, range=Optional[str])

slots.url = Slot(uri=SCHEMA.url, name="url", curie=SCHEMA.curie('url'),
                   model_uri=DATASET_AP.url, domain=None, range=Optional[str])

slots.variableMeasured = Slot(uri=SCHEMA.variableMeasured, name="variableMeasured", curie=SCHEMA.curie('variableMeasured'),
                   model_uri=DATASET_AP.variableMeasured, domain=None, range=Optional[str])

slots.version = Slot(uri=SCHEMA.version, name="version", curie=SCHEMA.curie('version'),
                   model_uri=DATASET_AP.version, domain=None, range=Optional[str])

slots.legalName = Slot(uri=SCHEMA.legalName, name="legalName", curie=SCHEMA.curie('legalName'),
                   model_uri=DATASET_AP.legalName, domain=None, range=Optional[str])

slots.mainEntityOfPage = Slot(uri=SCHEMA.mainEntityOfPage, name="mainEntityOfPage", curie=SCHEMA.curie('mainEntityOfPage'),
                   model_uri=DATASET_AP.mainEntityOfPage, domain=None, range=Optional[str])

slots.value = Slot(uri=SCHEMA.value, name="value", curie=SCHEMA.curie('value'),
                   model_uri=DATASET_AP.value, domain=None, range=Optional[str])

slots.valuereference = Slot(uri=SCHEMA.valuereference, name="valuereference", curie=SCHEMA.curie('valuereference'),
                   model_uri=DATASET_AP.valuereference, domain=None, range=Optional[str])

slots.unitCode = Slot(uri=SCHEMA.unitCode, name="unitCode", curie=SCHEMA.curie('unitCode'),
                   model_uri=DATASET_AP.unitCode, domain=None, range=Optional[str])

slots.unitText = Slot(uri=SCHEMA.unitText, name="unitText", curie=SCHEMA.curie('unitText'),
                   model_uri=DATASET_AP.unitText, domain=None, range=Optional[str])

slots.codeValue = Slot(uri=SCHEMA.codeValue, name="codeValue", curie=SCHEMA.curie('codeValue'),
                   model_uri=DATASET_AP.codeValue, domain=None, range=Optional[str])

slots.termCode = Slot(uri=SCHEMA.termCode, name="termCode", curie=SCHEMA.curie('termCode'),
                   model_uri=DATASET_AP.termCode, domain=None, range=Optional[str])

slots.inDefinedTermSet = Slot(uri=SCHEMA.inDefinedTermSet, name="inDefinedTermSet", curie=SCHEMA.curie('inDefinedTermSet'),
                   model_uri=DATASET_AP.inDefinedTermSet, domain=None, range=Optional[str])

slots.BioschemasDataset_alternateName = Slot(uri=SCHEMA.alternateName, name="BioschemasDataset_alternateName", curie=SCHEMA.curie('alternateName'),
                   model_uri=DATASET_AP.BioschemasDataset_alternateName, domain=BioschemasDataset, range=Optional[str])

slots.BioschemasDataset_citation = Slot(uri=SCHEMA.citation, name="BioschemasDataset_citation", curie=SCHEMA.curie('citation'),
                   model_uri=DATASET_AP.BioschemasDataset_citation, domain=BioschemasDataset, range=Optional[str])

slots.BioschemasDataset_creator = Slot(uri=SCHEMA.creator, name="BioschemasDataset_creator", curie=SCHEMA.curie('creator'),
                   model_uri=DATASET_AP.BioschemasDataset_creator, domain=BioschemasDataset, range=Optional[str])

slots.BioschemasDataset_dateCreated = Slot(uri=SCHEMA.dateCreated, name="BioschemasDataset_dateCreated", curie=SCHEMA.curie('dateCreated'),
                   model_uri=DATASET_AP.BioschemasDataset_dateCreated, domain=BioschemasDataset, range=Optional[str])

slots.BioschemasDataset_dateModified = Slot(uri=SCHEMA.dateModified, name="BioschemasDataset_dateModified", curie=SCHEMA.curie('dateModified'),
                   model_uri=DATASET_AP.BioschemasDataset_dateModified, domain=BioschemasDataset, range=Optional[str])

slots.BioschemasDataset_datePublished = Slot(uri=SCHEMA.datePublished, name="BioschemasDataset_datePublished", curie=SCHEMA.curie('datePublished'),
                   model_uri=DATASET_AP.BioschemasDataset_datePublished, domain=BioschemasDataset, range=Optional[str])

slots.BioschemasDataset_description = Slot(uri=SCHEMA.description, name="BioschemasDataset_description", curie=SCHEMA.curie('description'),
                   model_uri=DATASET_AP.BioschemasDataset_description, domain=BioschemasDataset, range=str)

slots.BioschemasDataset_distribution = Slot(uri=SCHEMA.distribution, name="BioschemasDataset_distribution", curie=SCHEMA.curie('distribution'),
                   model_uri=DATASET_AP.BioschemasDataset_distribution, domain=BioschemasDataset, range=Optional[str])

slots.BioschemasDataset_hasPart = Slot(uri=SCHEMA.hasPart, name="BioschemasDataset_hasPart", curie=SCHEMA.curie('hasPart'),
                   model_uri=DATASET_AP.BioschemasDataset_hasPart, domain=BioschemasDataset, range=Optional[str])

slots.BioschemasDataset_identifier = Slot(uri=SCHEMA.identifier, name="BioschemasDataset_identifier", curie=SCHEMA.curie('identifier'),
                   model_uri=DATASET_AP.BioschemasDataset_identifier, domain=BioschemasDataset, range=str)

slots.BioschemasDataset_includedInDataCatalog = Slot(uri=SCHEMA.includedInDataCatalog, name="BioschemasDataset_includedInDataCatalog", curie=SCHEMA.curie('includedInDataCatalog'),
                   model_uri=DATASET_AP.BioschemasDataset_includedInDataCatalog, domain=BioschemasDataset, range=Optional[str])

slots.BioschemasDataset_isAccessibleForFree = Slot(uri=SCHEMA.isAccessibleForFree, name="BioschemasDataset_isAccessibleForFree", curie=SCHEMA.curie('isAccessibleForFree'),
                   model_uri=DATASET_AP.BioschemasDataset_isAccessibleForFree, domain=BioschemasDataset, range=Optional[str])

slots.BioschemasDataset_isBasedOn = Slot(uri=SCHEMA.isBasedOn, name="BioschemasDataset_isBasedOn", curie=SCHEMA.curie('isBasedOn'),
                   model_uri=DATASET_AP.BioschemasDataset_isBasedOn, domain=BioschemasDataset, range=Optional[str])

slots.BioschemasDataset_isPartOf = Slot(uri=SCHEMA.isPartOf, name="BioschemasDataset_isPartOf", curie=SCHEMA.curie('isPartOf'),
                   model_uri=DATASET_AP.BioschemasDataset_isPartOf, domain=BioschemasDataset, range=Optional[str])

slots.BioschemasDataset_keywords = Slot(uri=SCHEMA.keywords, name="BioschemasDataset_keywords", curie=SCHEMA.curie('keywords'),
                   model_uri=DATASET_AP.BioschemasDataset_keywords, domain=BioschemasDataset, range=str)

slots.BioschemasDataset_license = Slot(uri=SCHEMA.license, name="BioschemasDataset_license", curie=SCHEMA.curie('license'),
                   model_uri=DATASET_AP.BioschemasDataset_license, domain=BioschemasDataset, range=str)

slots.BioschemasDataset_maintainer = Slot(uri=SCHEMA.maintainer, name="BioschemasDataset_maintainer", curie=SCHEMA.curie('maintainer'),
                   model_uri=DATASET_AP.BioschemasDataset_maintainer, domain=BioschemasDataset, range=Optional[str])

slots.BioschemasDataset_measurementTechnique = Slot(uri=SCHEMA.measurementTechnique, name="BioschemasDataset_measurementTechnique", curie=SCHEMA.curie('measurementTechnique'),
                   model_uri=DATASET_AP.BioschemasDataset_measurementTechnique, domain=BioschemasDataset, range=Optional[str])

slots.BioschemasDataset_name = Slot(uri=SCHEMA.name, name="BioschemasDataset_name", curie=SCHEMA.curie('name'),
                   model_uri=DATASET_AP.BioschemasDataset_name, domain=BioschemasDataset, range=str)

slots.BioschemasDataset_publisher = Slot(uri=SCHEMA.publisher, name="BioschemasDataset_publisher", curie=SCHEMA.curie('publisher'),
                   model_uri=DATASET_AP.BioschemasDataset_publisher, domain=BioschemasDataset, range=Optional[str])

slots.BioschemasDataset_sameAs = Slot(uri=SCHEMA.sameAs, name="BioschemasDataset_sameAs", curie=SCHEMA.curie('sameAs'),
                   model_uri=DATASET_AP.BioschemasDataset_sameAs, domain=BioschemasDataset, range=Optional[str])

slots.BioschemasDataset_url = Slot(uri=SCHEMA.url, name="BioschemasDataset_url", curie=SCHEMA.curie('url'),
                   model_uri=DATASET_AP.BioschemasDataset_url, domain=BioschemasDataset, range=str)

slots.BioschemasDataset_variableMeasured = Slot(uri=SCHEMA.variableMeasured, name="BioschemasDataset_variableMeasured", curie=SCHEMA.curie('variableMeasured'),
                   model_uri=DATASET_AP.BioschemasDataset_variableMeasured, domain=BioschemasDataset, range=Optional[str])

slots.BioschemasDataset_version = Slot(uri=SCHEMA.version, name="BioschemasDataset_version", curie=SCHEMA.curie('version'),
                   model_uri=DATASET_AP.BioschemasDataset_version, domain=BioschemasDataset, range=Optional[str])