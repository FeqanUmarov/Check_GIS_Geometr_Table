import arcpy

class Check_ZebtTorpaq:
    def __init__(self,base_data_path,error_data_path,trash_data_path):
        super().__init__()
        base_data_path = base_data_path + '\RAYON'

        self.check_zebt_torpaq(base_data_path,error_data_path,trash_data_path)
        
    
    def check_zebt_torpaq(self,base_data_path,error_data_path,trash_data_path):
        arcpy.management.MakeFeatureLayer(base_data_path+"\TORPAQ_TUM","Torpaq1")
        
        arcpy.management.MakeFeatureLayer(base_data_path+"\Zebt","Zebt2")
        
        arcpy.management.SelectLayerByAttribute("Torpaq1", 'NEW_SELECTION',"LEQAL_MI IS NULL AND SERHED_TIP IS NULL AND ISTIFADE IS NULL", 'NON_INVERT')
        
        arcpy.management.CopyFeatures("Torpaq1",trash_data_path+"\Leqalligi_Serhedtipi_Istifadesi_bos_olanlar")
        arcpy.management.SelectLayerByAttribute("Torpaq1", 'CLEAR_SELECTION')
        
        
        arcpy.management.SelectLayerByAttribute("Torpaq1", 'NEW_SELECTION',"T_KATEGORI = 0 and ALT_KATEGORI = 0 and MULKFORM = 0", 'NON_INVERT')
        arcpy.management.CopyFeatures("Torpaq1",trash_data_path+"\Torpaq2")
        arcpy.management.MakeFeatureLayer(trash_data_path+"\Torpaq2","Torpaq3")
        arcpy.management.SelectLayerByLocation('Torpaq3', 'CONTAINS', 'Zebt2','', 'NEW_SELECTION', 'NOT_INVERT')
        arcpy.management.SelectLayerByAttribute('Torpaq3', 'SWITCH_SELECTION')
        
        arcpy.management.CopyFeatures("Torpaq3",trash_data_path+"\Torpaq4")
        arcpy.management.MakeFeatureLayer(trash_data_path+"\Torpaq4","Torpaq5")
        arcpy.management.SelectLayerByAttribute("Torpaq5", 'NEW_SELECTION',"ACIKLAMA NOT LIKE '%Zept%' or ACIKLAMA NOT LIKE '%Zebt%' or ACIKLAMA NOT LIKE '%zept%' or ACIKLAMA NOT LIKE '%zebt%' or ACIKLAMA NOT LIKE '%zəbt%' or ACIKLAMA NOT LIKE '%Zəbt%' or ACIKLAMA NOT LIKE '%zəpt%' or ACIKLAMA NOT LIKE '%Zəpt%'", 'NON_INVERT')
        arcpy.management.SelectLayerByAttribute('Torpaq5', 'SWITCH_SELECTION')
        arcpy.management.CopyFeatures("Torpaq5",error_data_path+"\Torpagin_ustunde_zebt_yoxdur_aciqlamaya_zebt_yazilsin")
        
        
        arcpy.management.MakeFeatureLayer(base_data_path+"\TORPAQ_TUM","Torpaq6")
        arcpy.management.SelectLayerByAttribute("Torpaq6", 'NEW_SELECTION',"T_KATEGORI = 6 and MULKFORM = 1", 'NON_INVERT')
        arcpy.management.SelectLayerByAttribute('Torpaq6', 'SWITCH_SELECTION')
        arcpy.management.CopyFeatures("Torpaq6",trash_data_path+"\Torpaq7")
        arcpy.management.MakeFeatureLayer(trash_data_path+"\Torpaq7","Torpaq8")
        arcpy.management.SelectLayerByAttribute("Torpaq8", 'NEW_SELECTION',"ACIKLAMA LIKE '%bef%' or ACIKLAMA LIKE '%Bef%' or ACIKLAMA LIKE '%Bəf%' or ACIKLAMA LIKE '%bəf%' or ACIKLAMA LIKE '%BEF%' or ACIKLAMA LIKE '%Bef%' or ACIKLAMA LIKE '%bEf%' or ACIKLAMA LIKE '%beF%'", 'NON_INVERT')
        arcpy.management.CopyFeatures("Torpaq8",error_data_path+"\Aciqlamada_BEF_Yazilib_Kateqoriyasi_Ehtiyyat_Fondu_Deyil")
        
        
        print("Zebt torpaq check okey")

        
        
        
            
        