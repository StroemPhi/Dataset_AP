

CREATE TABLE "ChemicalEntity" (
	identifier TEXT NOT NULL, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	PRIMARY KEY (identifier)
);

CREATE TABLE "ChemicalReaction" (
	identifier TEXT NOT NULL, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	PRIMARY KEY (identifier)
);

CREATE TABLE "CreativeWork" (
	identifier TEXT NOT NULL, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	citation TEXT, 
	creator TEXT, 
	"dateCreated" TEXT, 
	"dateModified" TEXT, 
	"datePublished" TEXT, 
	"hasPart" TEXT, 
	"isAccessibleForFree" TEXT, 
	"isBasedOn" TEXT, 
	"isPartOf" TEXT, 
	keywords TEXT, 
	license TEXT, 
	maintainer TEXT, 
	publisher TEXT, 
	version TEXT, 
	PRIMARY KEY (identifier)
);

CREATE TABLE "DatasetCollection" (
	identifier TEXT NOT NULL, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	citation TEXT, 
	creator TEXT, 
	"dateCreated" TEXT, 
	"dateModified" TEXT, 
	"datePublished" TEXT, 
	"hasPart" TEXT, 
	"isAccessibleForFree" TEXT, 
	"isBasedOn" TEXT, 
	"isPartOf" TEXT, 
	keywords TEXT, 
	license TEXT, 
	maintainer TEXT, 
	publisher TEXT, 
	version TEXT, 
	datasets TEXT NOT NULL, 
	"measurementMethod" TEXT, 
	"measurementTechnique" TEXT, 
	PRIMARY KEY (identifier)
);

CREATE TABLE "Intangible" (
	identifier TEXT NOT NULL, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	PRIMARY KEY (identifier)
);

CREATE TABLE "MaterialEntity" (
	identifier TEXT NOT NULL, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	PRIMARY KEY (identifier)
);

CREATE TABLE "ReactionStep" (
	identifier TEXT NOT NULL, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	PRIMARY KEY (identifier)
);

CREATE TABLE "Thing" (
	identifier TEXT NOT NULL, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	PRIMARY KEY (identifier)
);

CREATE TABLE "Dataset" (
	identifier TEXT NOT NULL, 
	"sameAs" TEXT, 
	distribution TEXT, 
	"includedInDataCatalog" TEXT, 
	issn TEXT, 
	"measurementMethod" TEXT, 
	"measurementTechnique" TEXT, 
	"variableMeasured" TEXT, 
	"conformsTo" TEXT NOT NULL, 
	description TEXT NOT NULL, 
	keywords TEXT NOT NULL, 
	license TEXT NOT NULL, 
	name TEXT NOT NULL, 
	url TEXT NOT NULL, 
	citation TEXT, 
	creator TEXT, 
	"datePublished" TEXT, 
	"isBasedOn" TEXT, 
	publisher TEXT, 
	version TEXT, 
	"dateCreated" TEXT, 
	"dateModified" TEXT, 
	"hasPart" TEXT, 
	"isPartOf" TEXT, 
	"isAccessibleForFree" TEXT, 
	maintainer TEXT, 
	PRIMARY KEY (identifier), 
	FOREIGN KEY("includedInDataCatalog") REFERENCES "DatasetCollection" (identifier)
);

CREATE TABLE "ChemicalEntity_alternateName" (
	backref_id TEXT, 
	"alternateName" TEXT, 
	PRIMARY KEY (backref_id, "alternateName"), 
	FOREIGN KEY(backref_id) REFERENCES "ChemicalEntity" (identifier)
);

CREATE TABLE "ChemicalReaction_alternateName" (
	backref_id TEXT, 
	"alternateName" TEXT, 
	PRIMARY KEY (backref_id, "alternateName"), 
	FOREIGN KEY(backref_id) REFERENCES "ChemicalReaction" (identifier)
);

CREATE TABLE "CreativeWork_alternateName" (
	backref_id TEXT, 
	"alternateName" TEXT, 
	PRIMARY KEY (backref_id, "alternateName"), 
	FOREIGN KEY(backref_id) REFERENCES "CreativeWork" (identifier)
);

CREATE TABLE "DatasetCollection_alternateName" (
	backref_id TEXT, 
	"alternateName" TEXT, 
	PRIMARY KEY (backref_id, "alternateName"), 
	FOREIGN KEY(backref_id) REFERENCES "DatasetCollection" (identifier)
);

CREATE TABLE "Intangible_alternateName" (
	backref_id TEXT, 
	"alternateName" TEXT, 
	PRIMARY KEY (backref_id, "alternateName"), 
	FOREIGN KEY(backref_id) REFERENCES "Intangible" (identifier)
);

CREATE TABLE "MaterialEntity_alternateName" (
	backref_id TEXT, 
	"alternateName" TEXT, 
	PRIMARY KEY (backref_id, "alternateName"), 
	FOREIGN KEY(backref_id) REFERENCES "MaterialEntity" (identifier)
);

CREATE TABLE "ReactionStep_alternateName" (
	backref_id TEXT, 
	"alternateName" TEXT, 
	PRIMARY KEY (backref_id, "alternateName"), 
	FOREIGN KEY(backref_id) REFERENCES "ReactionStep" (identifier)
);

CREATE TABLE "Thing_alternateName" (
	backref_id TEXT, 
	"alternateName" TEXT, 
	PRIMARY KEY (backref_id, "alternateName"), 
	FOREIGN KEY(backref_id) REFERENCES "Thing" (identifier)
);

CREATE TABLE "Assay" (
	has_input TEXT, 
	has_output TEXT, 
	PRIMARY KEY (has_input, has_output), 
	FOREIGN KEY(has_output) REFERENCES "Dataset" (identifier)
);

CREATE TABLE "Dataset_alternateName" (
	backref_id TEXT, 
	"alternateName" TEXT, 
	PRIMARY KEY (backref_id, "alternateName"), 
	FOREIGN KEY(backref_id) REFERENCES "Dataset" (identifier)
);
