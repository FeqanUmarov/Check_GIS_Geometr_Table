import arcpy



class AUXILIARY_BUILDING:
    
    def __init__(self,base_data_path,output_data_path,checkbox_value,textBrowser,readme,head):
        super().__init__()
        base_data_path = base_data_path + '\RAYON'
        self.write_auxiliary_field(base_data_path,output_data_path,checkbox_value,textBrowser,readme,head)
        self.auxiliary_property_gr(output_data_path,checkbox_value,textBrowser,readme,head)
        self.auxiliary_delete_field(output_data_path,checkbox_value,textBrowser,readme,head)
    
    def write_auxiliary_field(self,base_data_path,output_data_path,checkbox_value,textBrowser,readme,head):
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor=textBrowser.textCursor()
        
        
        try:

            ################################## query ###################################
            fields = {'FK_AUXILIARY_TYPE':'!TIPI!','FK_PROPERTY_TYPE':5,'FK_OWNERSHIP_TYPE':'!Join_Tor_Komek.MULKFORM!','DESCRIPTION':'!ACIKLAMA!',
                    'FK_IS_LEGAL':'!Join_Tor_Komek.LEQAL_MI!','BUILDING_AREA':'round(!SHAPE_Area!,0)'}
            arcpy.management.CopyFeatures(base_data_path+'\KOMEKCI',output_data_path+"\AUXILIARY_BUILDING")
            arcpy.analysis.SpatialJoin(base_data_path+'\TORPAQ_TUM', base_data_path+'\TIKILI_TUM',output_data_path+"\Join_Tor_Tikli", 'JOIN_ONE_TO_ONE', 'KEEP_ALL',"", 'INTERSECT')
            arcpy.analysis.SpatialJoin(output_data_path+"\AUXILIARY_BUILDING", output_data_path+"\Join_Tor_Tikli",output_data_path+"\Join_Tor_Komek", 'JOIN_ONE_TO_ONE', 'KEEP_ALL',"", 'INTERSECT')

            for key,value in fields.items():
                if key == 'FK_AUXILIARY_TYPE':
                    arcpy.management.AddField(output_data_path+"\AUXILIARY_BUILDING",key, 'SHORT')
                    arcpy.management.CalculateField(output_data_path+"\AUXILIARY_BUILDING", key,value, 'PYTHON3')
                if key == 'BUILDING_AREA':
                    arcpy.management.AddField(output_data_path+"\AUXILIARY_BUILDING",key, 'DOUBLE')
                    arcpy.management.CalculateField(output_data_path+"\AUXILIARY_BUILDING", key,value, 'PYTHON3')

                if key == 'FK_PROPERTY_TYPE':
                    arcpy.management.AddField(output_data_path+"\AUXILIARY_BUILDING",key, 'SHORT')
                    arcpy.management.CalculateField(output_data_path+"\AUXILIARY_BUILDING", key,value, 'PYTHON3')

                if key == "FK_OWNERSHIP_TYPE":
                    arcpy.management.AddField(output_data_path+"\AUXILIARY_BUILDING",key, 'SHORT')
                    arcpy.management.MakeFeatureLayer(output_data_path+"\AUXILIARY_BUILDING","make_join5")
                    arcpy.management.AddJoin('make_join5', 'OBJECTID', output_data_path+"\Join_Tor_Komek", 'TARGET_FID_1', 'KEEP_ALL')
                    arcpy.management.CalculateField("make_join5", key,value, 'PYTHON3')
                    arcpy.management.RemoveJoin("make_join5", 'Join_Tor_Komek')

                if key == "FK_IS_LEGAL":
                    arcpy.management.AddField(output_data_path+"\AUXILIARY_BUILDING",key, 'SHORT')
                    arcpy.management.MakeFeatureLayer(output_data_path+"\AUXILIARY_BUILDING","make_join6")
                    arcpy.management.AddJoin('make_join6', 'OBJECTID', output_data_path+"\Join_Tor_Komek", 'TARGET_FID_1', 'KEEP_ALL')
                    arcpy.management.CalculateField("make_join6", key,value, 'PYTHON3')
                    arcpy.management.RemoveJoin("make_join6", 'Join_Tor_Komek')
                    
                if key == "DESCRIPTION":
                    arcpy.management.AddField(output_data_path+"\AUXILIARY_BUILDING",key, 'TEXT')
                    arcpy.management.CalculateField(output_data_path+"\AUXILIARY_BUILDING", key,value, 'PYTHON3')
                    
                  
            arcpy.analysis.SpatialJoin(output_data_path+'\AUXILIARY_BUILDING',base_data_path+'\QUARTER',output_data_path+'\Aux_Quarter','JOIN_ONE_TO_ONE', 'KEEP_ALL','','WITHIN')
            arcpy.management.AlterField(output_data_path+'\Aux_Quarter', 'QUARTER_NAME',"ADDRESS","ADDRESS", 'TEXT')  
                    
            if checkbox_value:
                readme.write("\n")
                readme.write("\n13. Komekcide yeni sutunlar yaradildi ve kohne sutunlarda olan melumatlar kocuruldu")
            cursor.insertHtml('''<p><span style="color:green;">Köməkçidə yeni sütunlar yaradıldı və köhnə sütunlarda olan məlumatlar
                                  köçürüldü. <br> </span>''')
                    
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n13. Komekcide yeni sutunlarin yaradilmasinda ve melumatlarin yaradilmasinda xeta bas verdi. Araliq bazadaki sutun adlarina ve tiplerine nezer yetirin!")
            cursor.insertHtml('''<p><span style="color:red;">Köməkçidə yeni sütunların yaradılmasında və məlumanların yazılmasında xəta baş verdi.
                                  Aralıq bazadakı sütun adlarına və tiplərinə nəzər yetirin! <br> </span>''')
                
        if checkbox_value:         
            readme.close()  
            
            
            
                
                
                
        ################################## query ####################################

    def auxiliary_property_gr(self,output_data_path,checkbox_value,textBrowser,readme,head):
        ################################## AUXILIARY property export ####################################
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor=textBrowser.textCursor()
        
        try:
        
            arcpy.conversion.ExportTable(output_data_path+'\Aux_Quarter',output_data_path+"\AUXILIARY_Property")
            building_property_fields = arcpy.ListFields(output_data_path+"\AUXILIARY_Property")
            require_Buil_Field_name = ["OBJECTID","REGISTER_NO","FK_PROPERTY_TYPE","FK_OWNERSHIP_TYPE","TOTAL_AREA",
                                    "ADDRESS","DESCRIPTION","FK_IS_LEGAL"]

            list_BUİL_PORPERTY_field = []

            for field in building_property_fields:
                list_BUİL_PORPERTY_field.append(field.name)

            for Buil_Table_Field_N in list_BUİL_PORPERTY_field:
                if Buil_Table_Field_N not in require_Buil_Field_name:
                    arcpy.management.DeleteField(output_data_path+"\AUXILIARY_Property",Buil_Table_Field_N)
                    
                    
            if checkbox_value:
                readme.write("\n")
                readme.write("\n14 .Property Group (komekci) ucun lazimi melumatlar export edildi")
            cursor.insertHtml('''<p><span style="color:green;">Property group (köməkçi) üçün lazımı məlumatlar export edildi. <br> </span>''')
                    
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n14. Property Group (komekci) cedveli export edile bilmedi. Araliq bazada olan Komekci layinin sutun adlarinin dogru olduguna diqqet edin!")
            cursor.insertHtml('''<p><span style="color:red;">Property Group (köməkçi) cədvəli export edilə bilmədi. Aralıq bazada olan
                              Köməkçi layının sütun adlarının doğru olduğuna diqqət edin! <br> </span>''')
            
        if checkbox_value:     
            readme.close()


        ################################## AUXILIARY property export ####################################

    def auxiliary_delete_field(self,output_data_path,checkbox_value,textBrowser,readme,head):
        ################################## delete field ####################################
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor=textBrowser.textCursor()
        
        try:

            AUXILIARY_Field = ["FK_AUXILIARY_TYPE","BUILDING_AREA"]
                    
            AUXILIARY_fields = arcpy.ListFields(output_data_path+"\AUXILIARY_BUILDING")
            list_AUXILIARY_field = []

            for field in AUXILIARY_fields:
                list_AUXILIARY_field.append(field.name)


            for s in list_AUXILIARY_field:
                if (s not in AUXILIARY_Field) and (s!="OBJECTID" and s!="SHAPE" and s!="SHAPE_Length" and s!="SHAPE_Area"):
                    arcpy.management.DeleteField(output_data_path+"\AUXILIARY_BUILDING",s)
                    
                    
            if checkbox_value:
                readme.write("\n")
                readme.write("\n15. Komekciden lazimsiz sutunlar silindi")
            cursor.insertHtml('''<p><span style="color:green;">Köməkçi-dən lazımsız sütunlar silindi. <br> </span>''')
            cursor.insertHtml('''<p><span style="color:black;"> <strong>-----------------------------------------------------------</strong> <br> </span>''')
                    
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n15. Komekciden lazimsiz sutunlar siline bilmedi. Neticlerin gonderildiyi bazanin movcud olduguna ve ya basqa proqram terefinden istifade edilmediyinden emin olun")
            cursor.insertHtml('''<p><span style="color:red;">Köməkçidən lazımsız sütunlar silinə bilmədi. Nəticələrin
                              göndərildiyi bazanın mövcdu olduğundan və ya bazanın başqa proqram tərəfindən məşğul edilmədiyindən
                              əmin olun. <br> </span>''')
            cursor.insertHtml('''<p><span style="color:black;"> <strong>-----------------------------------------------------------</strong> <br> </span>''')

        ################################## delete field ####################################
        if checkbox_value: 
            readme.close()
        



    

