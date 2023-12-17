

CREATE TABLE "BioschemasDataset" (
	"alternateName" TEXT, 
	citation TEXT, 
	creator TEXT, 
	"dateCreated" TEXT, 
	"dateModified" TEXT, 
	"datePublished" TEXT, 
	description TEXT NOT NULL, 
	distribution TEXT, 
	"hasPart" TEXT, 
	identifier TEXT NOT NULL, 
	"includedInDataCatalog" TEXT, 
	"isAccessibleForFree" TEXT, 
	"isBasedOn" TEXT, 
	"isPartOf" TEXT, 
	keywords TEXT NOT NULL, 
	license TEXT NOT NULL, 
	maintainer TEXT, 
	"measurementTechnique" TEXT, 
	name TEXT NOT NULL, 
	publisher TEXT, 
	"sameAs" TEXT, 
	url TEXT NOT NULL, 
	"variableMeasured" TEXT, 
	version TEXT, 
	PRIMARY KEY ("alternateName", citation, creator, "dateCreated", "dateModified", "datePublished", description, distribution, "hasPart", identifier, "includedInDataCatalog", "isAccessibleForFree", "isBasedOn", "isPartOf", keywords, license, maintainer, "measurementTechnique", name, publisher, "sameAs", url, "variableMeasured", version)
);

CREATE TABLE "CategoryCode" (
	name TEXT, 
	"codeValue" TEXT, 
	url TEXT, 
	PRIMARY KEY (name, "codeValue", url)
);

CREATE TABLE "CreativeWork" (
	name TEXT, 
	identifier TEXT, 
	url TEXT, 
	PRIMARY KEY (name, identifier, url)
);

CREATE TABLE "DataCatalog" (
	name TEXT, 
	PRIMARY KEY (name)
);

CREATE TABLE "DataDownload" (
	name TEXT, 
	PRIMARY KEY (name)
);

CREATE TABLE "DateTime" (
	name TEXT, 
	PRIMARY KEY (name)
);

CREATE TABLE "DefinedTerm" (
	url TEXT, 
	name TEXT, 
	"termCode" TEXT, 
	identifier TEXT, 
	"inDefinedTermSet" TEXT, 
	PRIMARY KEY (url, name, "termCode", identifier, "inDefinedTermSet")
);

CREATE TABLE "DefinedTermSet" (
	name TEXT, 
	identifier TEXT, 
	url TEXT, 
	PRIMARY KEY (name, identifier, url)
);

CREATE TABLE "Organization" (
	name TEXT, 
	"legalName" TEXT, 
	description TEXT, 
	"sameAs" TEXT, 
	PRIMARY KEY (name, "legalName", description, "sameAs")
);

CREATE TABLE "Person" (
	name TEXT, 
	url TEXT, 
	"mainEntityOfPage" TEXT, 
	PRIMARY KEY (name, url, "mainEntityOfPage")
);

CREATE TABLE "Product" (
	name TEXT, 
	PRIMARY KEY (name)
);

CREATE TABLE "PropertyValue" (
	name TEXT, 
	value TEXT, 
	identifier TEXT, 
	valuereference TEXT, 
	"unitCode" TEXT, 
	"unitText" TEXT, 
	PRIMARY KEY (name, value, identifier, valuereference, "unitCode", "unitText")
);

CREATE TABLE "Trip" (
	name TEXT, 
	PRIMARY KEY (name)
);
