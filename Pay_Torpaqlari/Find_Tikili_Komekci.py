import arcpy

class check_Tikili_Komekci:
    def __init__(self,base_data_path,error_data_path):
        super().__init__()
        base_data_path = base_data_path + '\RAYON'

        self.Tikili_Komekci(base_data_path,error_data_path)
        
    
    def Tikili_Komekci(self,base_data_path,error_data_path):
        
        arcpy.management.MakeFeatureLayer(base_data_path+"\TORPAQ_TUM","Torpaq12")
        arcpy.management.MakeFeatureLayer(base_data_path+"\Tikili_Azcad","Tikili_Azcad1")
        check_az_tikili = arcpy.management.SelectLayerByLocation('Tikili_Azcad1', 'WITHIN', 'Torpaq12','', 'NEW_SELECTION', 'NOT_INVERT')
        
        count_az_tikili = arcpy.GetCount_management(check_az_tikili)
        
        if str(count_az_tikili) !="0":
            arcpy.management.CopyFeatures("Tikili_Azcad1",error_data_path+"\Azcadda_Movcud_Olan_Tikililer")
            
            
        
        arcpy.management.MakeFeatureLayer(base_data_path+"\Komekci_Azcad","Komekci_Azcad1")
        check_az_komekci = arcpy.management.SelectLayerByLocation('Komekci_Azcad1', 'WITHIN', 'Torpaq12','', 'NEW_SELECTION', 'NOT_INVERT')
        
        count_az_komekci = arcpy.GetCount_management(check_az_komekci)
        
        if str(count_az_komekci) !="0":
            arcpy.management.CopyFeatures("Komekci_Azcad1",error_data_path+"\Azcadda_Movcud_Olan_Komekciler")
            
            
        