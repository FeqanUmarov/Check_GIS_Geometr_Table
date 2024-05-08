import arcpy

class deleteEmpty_layer:
    def __init__(self,error_data_path):
        super().__init__()

        self.deleteEmpty(error_data_path)
        
    
    def deleteEmpty(self,error_data_path):
        
        arcpy.env.workspace = error_data_path
        
        list_feature  = arcpy.arcpy.ListFeatureClasses("*")
        for fc in list_feature:
            count_obj = str(arcpy.GetCount_management(fc))
            
            if count_obj == "0":
                arcpy.management.Delete(fc)
            
        