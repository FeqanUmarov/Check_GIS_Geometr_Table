import arcpy

class Pay_Zebt_check:
    def __init__(self,base_data_path,error_data_path,trash_data_path):
        super().__init__()
        base_data_path = base_data_path + '\RAYON'

        self.pay_zebt(base_data_path,error_data_path,trash_data_path)
        
    
    def pay_zebt(self,base_data_path,error_data_path,trash_data_path):
        
        arcpy.management.MakeFeatureLayer(base_data_path + "\Zebt","Zebt_yeni")
        arcpy.management.MakeFeatureLayer(base_data_path + "\Zebt_Kohne","Zebt_kohne")
        arcpy.management.MakeFeatureLayer(base_data_path + "\Pay_torpaqi","PayYeni")
        
        ########### Kohne zebtler yeni zebtlerle kesisirler ############
        arcpy.management.SelectLayerByLocation("Zebt_kohne", 'INTERSECT', "Zebt_yeni",'-1', 'NEW_SELECTION', 'NOT_INVERT')
        
        arcpy.management.CopyFeatures("Zebt_kohne",error_data_path+"\Kohne_Zebtlerle_Yeni_Zebtler_Kesisirler")
        
        arcpy.management.DeleteRows("Zebt_kohne")
        
        arcpy.management.SelectLayerByAttribute("Zebt_kohne", 'CLEAR_SELECTION')
        
        
        ########### Paylar kesisir zebtlerle ############
        arcpy.management.SelectLayerByLocation("Zebt_kohne", 'INTERSECT', "PayYeni",'-1', 'NEW_SELECTION', 'NOT_INVERT')
        
        arcpy.management.CopyFeatures("Zebt_kohne",error_data_path+"\Kohne_Zebtlerle_Paylar_Kesisirler")
        
        arcpy.management.DeleteRows("Zebt_kohne")
        
        
        ############ append zebtler ############
        
        arcpy.management.CopyFeatures(base_data_path +"\Zebt_Kohne",trash_data_path+"\Kohne_Zebt_Copy")
        
        arcpy.management.Append(base_data_path +"\Zebt",trash_data_path+"\Kohne_Zebt_Copy", 'NO_TEST')
        
        arcpy.management.CopyFeatures(trash_data_path+"\Kohne_Zebt_Copy",trash_data_path+"\Zebt_butov")
        
        arcpy.management.MakeFeatureLayer(trash_data_path+"\Zebt_butov","Zebt_butov_make")
        
        arcpy.management.MakeFeatureLayer(trash_data_path+"\Birlesmis_Torpaq","Birlesmis_Torpaq_Meke2")
        
        arcpy.management.SelectLayerByLocation("Zebt_butov_make", 'ARE_IDENTICAL_TO', "Birlesmis_Torpaq_Meke2",'', 'NEW_SELECTION', 'NOT_INVERT')
        
        arcpy.management.SelectLayerByAttribute('Zebt_butov_make', 'SWITCH_SELECTION')
        
        arcpy.analysis.Intersect([base_data_path+"\TORPAQ_TUM",'Zebt_butov_make'],error_data_path+"\inter", 'ALL')
        
        # arcpy.management.CopyFeatures("Zebt_butov_make",error_data_path+"\Torpaqla_Identic_Olmayan_Zebtler")
        
        
        ############### Payin altindaki torpaqlar (xususi olmasi yoxlanilacaq) ############
        
        arcpy.analysis.Clip(trash_data_path+"\Birlesmis_Torpaq", trash_data_path+"\Butov_pay",trash_data_path+"\Torpaq_Pay_Clip")
        
        arcpy.management.MakeFeatureLayer(trash_data_path+"\Torpaq_Pay_Clip","Torpaq_Pay_Clip_make")
        
        arcpy.management.SelectLayerByAttribute("Torpaq_Pay_Clip_make",'NEW_SELECTION',"MULKFORM <> 2", 'NON_INVERT')
        
        arcpy.management.CopyFeatures("Torpaq_Pay_Clip_make",error_data_path+"\Pay_Torpaqlarinin_altindaki_Torpaq_Xususi_Olmalidir")
        
        
        
        ############### Zebtin altindaki torpaqlar (dovlet olmasi yoxlanilacaq) ############
        
        arcpy.analysis.Clip(trash_data_path+"\Birlesmis_Torpaq", trash_data_path+"\Zebt_butov",trash_data_path+"\Torpaq_Zebt_Clip")
        
        arcpy.management.MakeFeatureLayer(trash_data_path+"\Torpaq_Zebt_Clip","Torpaq_Zebt_Clip_make")
        
        arcpy.management.SelectLayerByAttribute("Torpaq_Zebt_Clip_make",'NEW_SELECTION',"MULKFORM <> 0", 'NON_INVERT')
        
        arcpy.management.CopyFeatures("Torpaq_Zebt_Clip_make",error_data_path+"\Zebt_Torpaqlarinin_altindaki_Torpaq_Dovlet_Olmalidir")
        
        arcpy.management.SelectLayerByAttribute("Torpaq_Zebt_Clip_make", 'CLEAR_SELECTION')
        
        arcpy.management.SelectLayerByAttribute("Torpaq_Zebt_Clip_make",'NEW_SELECTION',"DESCRIPTION LIKE '%Zept%' or DESCRIPTION LIKE '%Zebt%' or DESCRIPTION LIKE '%zept%' or DESCRIPTION LIKE '%zebt%' or DESCRIPTION LIKE '%zəbt%' or DESCRIPTION LIKE '%Zəbt%' or DESCRIPTION LIKE '%zəpt%' or DESCRIPTION LIKE '%Zəpt%'", 'NON_INVERT')
        
        arcpy.management.CopyFeatures("Torpaq_Zebt_Clip_make",error_data_path+"\Zebt_Torpagin_Uzerinde_Movcuddur_Torpagin_Aciklamasinda_Zebt_Silinmelidir")