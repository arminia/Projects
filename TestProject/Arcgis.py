import arcpy

arcpy.CreateEnterpriseGeodatabase_management("SQL_SERVER", "tor\ssinstance1", "sp_data", "OPERATING_SYSTEM_AUTH", "", "", "SDE_SCHEMA", "sde", "sde",
                                             "", "//myserver/Program Files/ESRI/License10.1/sysgen/keycodes")