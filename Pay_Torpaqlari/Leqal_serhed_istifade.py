import arcpy

class CheckTorpaqAttLeqalIstSerhed:
    def __init__(self,base_data_path,error_data_path):
        super().__init__()
        base_data_path = base_data_path + '\RAYON'

        self.Check_leqal_serh_Ist(base_data_path,error_data_path)
        
    
    def Check_leqal_serh_Ist(self,base_data_path,error_data_path):
        arcpy.management.MakeFeatureLayer(base_data_path+"\TORPAQ_TUM","Torpaq11")
        arcpy.management.SelectLayerByAttribute("Torpaq11", 'NEW_SELECTION',"LEQAL_MI IS NULL and SERHED_TIP IS NULL and ISTIFADE IS NULL", 'NON_INVERT')
        arcpy.management.CopyFeatures("Torpaq11",error_data_path+"\Leqalligi_Serhedtipi_ve_Istifadesi_bos_olanlar")
        
            
            
        