import arcpy

class Covered_tikilitorpaq:
    def __init__(self,base_data_path,error_data_path):
        super().__init__()
        base_data_path = base_data_path + '\RAYON'

        self.Tikili_Covered_torpaq(base_data_path,error_data_path)
        
    
    def Tikili_Covered_torpaq(self,base_data_path,error_data_path):
        
        arcpy.management.MakeFeatureLayer(base_data_path+"\TORPAQ_TUM","Torpaq13")
        arcpy.management.MakeFeatureLayer(base_data_path+"\TIKILI_TUM","Tikili10")
        
        arcpy.management.SelectLayerByLocation('Tikili10', 'WITHIN', 'Torpaq13','', 'NEW_SELECTION', 'NOT_INVERT')
        
        check_tikili = arcpy.management.SelectLayerByAttribute("Tikili10", 'SWITCH_SELECTION')
        
        count_tikili = arcpy.GetCount_management(check_tikili)
        
        if str(count_tikili) != "0":
            arcpy.management.CopyFeatures("Tikili10",error_data_path+"\Tikili_Torpaqdan_Kenara_Cixir")
            
            
            
        arcpy.management.MakeFeatureLayer(base_data_path+"\KOMEKCI","Komekci9")
        
        arcpy.management.SelectLayerByLocation('Komekci9', 'WITHIN', 'Torpaq13','', 'NEW_SELECTION', 'NOT_INVERT')
        
        check_tikili = arcpy.management.SelectLayerByAttribute("Komekci9", 'SWITCH_SELECTION')
        
        count_tikili = arcpy.GetCount_management(check_tikili)
        
        if str(count_tikili) != "0":
            arcpy.management.CopyFeatures("Komekci9",error_data_path+"\Komekci_Torpaqdan_Kenara_Cixir")
            
            
        print("Covered tikili torpaq okey")