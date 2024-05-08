import arcpy

class Building:
    
    def __init__(self,base_data_path,output_data_path,checkbox_value,textBrowser,readme,head):
        super().__init__()
        base_data_path = base_data_path + '\RAYON'
        self.write_building_field(base_data_path,output_data_path,checkbox_value,textBrowser,readme,head)
        self.building_property_gr(output_data_path,checkbox_value,textBrowser,readme,head)
        self.building_certificate(output_data_path,checkbox_value,textBrowser,readme,head)
        self.building_property_ow(output_data_path,checkbox_value,textBrowser,readme,head)
        self.building_owner(output_data_path,checkbox_value,textBrowser,readme,head)
        self.building_delete_field(output_data_path,checkbox_value,textBrowser,readme,head)

    def write_building_field(self,base_data_path,output_data_path,checkbox_value,textBrowser,readme,head):
        ################################## query ###################################
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor=textBrowser.textCursor()
        
        

        fields = {'FK_BUILDING_NAME':'!TIKILI_NOVU!','FK_CONSTRUCTION_MAT_TYPE':'!MATERYAL!',
                    'FK_ROOF_TYPE':'!DAM_NOVU!','FK_IS_INCOMPLETE':'!YARIMCIQ!','FK_HAS_HEATING':'!ISTI_SU!',
                    'FK_HAS_GAS':'!QAZ!','FK_HAS_ELECTRICITY':'!ISIK!','FK_HAS_COLD_WATER':'!SU!',
                    'FK_HAS_WARM_WATER':'!ISTI_SU!','FK_HAS_SEWAGE_WATER':'!KANALIZASIYA!',
                    'FK_HAS_TELEPHONE':'!TELEFON!','FLOOR_COUNT':'!MERTEBE!','ROOM_COUNT':'!OTAQ_SAYISI!',
                    'BUILDING_AREA':'!SAHE!','REAL_AREA':'round(!SHAPE_Area!,0)','DESCRIPTION':'!ACIKLAMA!',
                    'BUILDING_YEAR':'!TIKILI_ILI!','BUILDING_NO':'!TIKILI_NO!','REGISTER_NO':'!REYESTR_NO!','FK_PROPERTY_TYPE':'!Torpaq_Tikili.EMLAK_NOVU!',
                    'FK_OWNERSHIP_TYPE':'!MULKFORM!','TOTAL_AREA':'!SAHE!','ADDRESS':'!UNVAN!','FK_IS_LEGAL':'!LEQAL_MI!',
                    'CERTIFICATION_DATE':'!SENED_TARIXI!','CERTIFICATION_NO':'!SENEDNO!','FK_CERTIFICATION_TYPE':'!SENEDNOVU!',
                    'FILE_PATH':'!SENEDSEKIL!','DURATON_OF_USE':'!Torpaq_Tikili.ISTIFADE_MUDDETI!','FULL_NAME':'!FULL_NAME!',
                    'DATE_OF_BIRTH':'!DOGUM_TARIXI!','ID_CARD_NUMBER':'!VESIKA_NOMRESI!','FK_RIGHT_TYPE':'!ISTIFADE!'}

        short_field = ['FK_BUILDING_NAME','FK_CONSTRUCTION_MAT_TYPE','FK_ROOF_TYPE','FK_IS_INCOMPLETE','FK_HAS_HEATING',
                        'FK_HAS_GAS','FK_HAS_ELECTRICITY','FK_HAS_COLD_WATER','FK_HAS_WARM_WATER','FK_HAS_SEWAGE_WATER','FK_HAS_TELEPHONE',
                        'FLOOR_COUNT','ROOM_COUNT','FK_OWNERSHIP_TYPE','FK_IS_LEGAL','FK_RIGHT_TYPE','BUILDING_YEAR']

        text_field = ['DESCRIPTION','BUILDING_NO','REGISTER_NO','ADDRESS','CERTIFICATION_NO','FILE_PATH','DURATON_OF_USE','FULL_NAME',
                        'ID_CARD_NUMBER']

        double_field = ['BUILDING_AREA','REAL_AREA','TOTAL_AREA']

        date_field = ['CERTIFICATION_DATE','DATE_OF_BIRTH']

        long_field = ['FK_PROPERTY_TYPE']
        try:

            arcpy.management.CopyFeatures(base_data_path+'\TIKILI_TUM',output_data_path+"\BUILDING")
            print("copy oldu tikilide")
          
            arcpy.analysis.Intersect([output_data_path+"\BUILDING",base_data_path+'\TORPAQ_TUM'],output_data_path+"\Torpaq_Tikili", 'ALL')
            print("intersect olmadi tikilide")

            for key,value in fields.items():
                if key in short_field:
                    arcpy.management.AddField(output_data_path+"\BUILDING",key, 'SHORT')
                    arcpy.management.CalculateField(output_data_path+"\BUILDING", key,value, 'PYTHON3')
                    
                if key in double_field:
                    arcpy.management.AddField(output_data_path+"\BUILDING",key, 'DOUBLE')
                    arcpy.management.CalculateField(output_data_path+"\BUILDING", key,value, 'PYTHON3')

                if key in date_field:
                    arcpy.management.AddField(output_data_path+"\BUILDING",key, 'DATE')
                    arcpy.management.CalculateField(output_data_path+"\BUILDING", key,value, 'PYTHON3')

                if key in text_field:
                    if key == 'DURATON_OF_USE':
                        arcpy.management.AddField(output_data_path+"\BUILDING",key, 'TEXT')
                        arcpy.management.MakeFeatureLayer(output_data_path+"\BUILDING","make_join1")
                        arcpy.management.AddJoin("make_join1", 'OBJECTID',output_data_path+"\Torpaq_Tikili" , 'FID_BUILDING')
                        arcpy.management.CalculateField("make_join1", key,value, 'PYTHON3')
                        arcpy.management.RemoveJoin("make_join1", 'Torpaq_Tikili')
                    else:
                        arcpy.management.AddField(output_data_path+"\BUILDING",key, 'TEXT')
                        arcpy.management.CalculateField(output_data_path+"\BUILDING", key,value, 'PYTHON3')

                if key in long_field:
                    arcpy.management.AddField(output_data_path+"\BUILDING",key, 'LONG')
                    arcpy.management.MakeFeatureLayer(output_data_path+"\BUILDING","make_join2")
                    arcpy.management.AddJoin("make_join2", 'OBJECTID',output_data_path+"\Torpaq_Tikili" ,'FID_BUILDING')
                    arcpy.management.CalculateField("make_join2", key,value, 'PYTHON3')
                    arcpy.management.RemoveJoin("make_join2", 'Torpaq_Tikili')

            if checkbox_value:
                readme.write("\n")
                readme.write("\n7. Tikilide yeni sutunlar yaradildi ve kohne sutunlarda olan melumatlar kocuruldu")
            cursor.insertHtml('''<p><span style="color:green;">Tikilidə yeni sütunlar yaradıldı və köhnə sütunlarda olan məlumatlar
                                  köçürüldü. <br> </span>''')
            
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n7. Tikilide yeni sutunlarin yaradilmasinda ve melumatlarin yaradilmasinda xeta bas verdi. Araliq bazadaki sutun adlarina ve tiplerine nezer yetirin!")
            cursor.insertHtml('''<p><span style="color:red;">Tikilidə yeni sütunların yaradılmasında və məlumanların yazılmasında xəta baş verdi.
                                  Aralıq bazadakı sütun adlarına və tiplərinə nəzər yetirin! <br> </span>''')
        
        if checkbox_value:    
            readme.close()
                
                    
                
        ################################## query ####################################
    def building_property_gr(self,output_data_path,checkbox_value,textBrowser,readme,head):
        ################################## Building property export ####################################
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor=textBrowser.textCursor()
        try:
        
            arcpy.conversion.ExportTable(output_data_path+"\BUILDING",output_data_path+"\Building_Property")
            building_property_fields = arcpy.ListFields(output_data_path+"\Building_Property")
            require_Buil_Field_name = ["OBJECTID","REGISTER_NO","FK_PROPERTY_TYPE","FK_OWNERSHIP_TYPE","TOTAL_AREA",
                                    "ADDRESS","DESCRIPTION","FK_IS_LEGAL"]

            list_BUİL_PORPERTY_field = []

            for field in building_property_fields:
                list_BUİL_PORPERTY_field.append(field.name)

            for Buil_Table_Field_N in list_BUİL_PORPERTY_field:
                if Buil_Table_Field_N not in require_Buil_Field_name:
                    arcpy.management.DeleteField(output_data_path+"\Building_Property",Buil_Table_Field_N)
                    
            if checkbox_value:
                readme.write("\n")
                readme.write("\n8. Property Group (tikili) ucun lazimi melumatlar export edildi")
            cursor.insertHtml('''<p><span style="color:green;">Property group (tikili) üçün lazımı məlumatlar export edildi. <br> </span>''')
                    
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n8. Property Group (tikili) cedveli export edile bilmedi. Araliq bazada olan Tikili tum layinin sutun adlarinin dogru olduguna diqqet edin!")
            cursor.insertHtml('''<p><span style="color:red;">Property Group (tikili) cədvəli export edilə bilmədi. Aralıq bazada olan
                              Tikili tum layının sütun adlarının doğru olduğuna diqqət edin! <br> </span>''')
        
        if checkbox_value:    
            readme.close()


        ################################## Building property export ####################################

    def building_certificate(self,output_data_path,checkbox_value,textBrowser,readme,head):
        ################################## Building Certificate export ####################################
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor=textBrowser.textCursor()
        try:
            arcpy.conversion.ExportTable(output_data_path+"\BUILDING",output_data_path+"\Building_Certificate")
            building_certificate_fields = arcpy.ListFields(output_data_path+"\Building_Property")

            require_Buil_Field_name = ["OBJECTID","CERTIFICATION_DATE","CERTIFICATION_NO","FK_CERTIFICATION_TYPE",
                                    "FILE_PATH","DURATON_OF_USE"]

            list_BUİL_PORPERTY_field = []

            for field in building_certificate_fields:
                list_BUİL_PORPERTY_field.append(field.name)
                
            for Buil_Table_Field_N in list_BUİL_PORPERTY_field:
                if Buil_Table_Field_N not in require_Buil_Field_name:
                    arcpy.management.DeleteField(output_data_path+"\Building_Certificate",Buil_Table_Field_N)
                    
            if checkbox_value:
                readme.write("\n")
                readme.write("\n9. Certificate (tikili) ucun lazimi melumatlar export edildi")
            cursor.insertHtml('''<p><span style="color:green;">Certificate (tikili) üçün lazımı məlumatlar export edildi. <br> </span>''')
     
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n9. Certificate (tikili) cedveli export edile bilmedi. Araliq bazada olan Tikili tum layinin sutun adlarinin dogru olduguna diqqet edin!")
            cursor.insertHtml('''<p><span style="color:red;">Certificate (tikili) cədvəli export edilə bilmədi. Aralıq bazada olan
                              Tikili tum layının sütun adlarının doğru olduğuna diqqət edin! <br> </span>''')
            
        if checkbox_value:    
            readme.close()
            


        ################################## Building Certificate export ####################################

    def building_property_ow(self,output_data_path,checkbox_value,textBrowser,readme,head):
        ################################## Building Property Owner export ####################################
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor=textBrowser.textCursor()

        try:
            arcpy.conversion.ExportTable(output_data_path+"\BUILDING",output_data_path+"\Building_Property_Owner")
            building_property_owner_fields = arcpy.ListFields(output_data_path+"\Building_Property_Owner")

            require_Buil_Field_name = ["OBJECTID","FK_RIGHT_TYPE"]

            list_BUİL_PORPERTY_field = []

            for field in building_property_owner_fields:
                list_BUİL_PORPERTY_field.append(field.name)
                
            for Buil_Table_Field_N in list_BUİL_PORPERTY_field:
                if Buil_Table_Field_N not in require_Buil_Field_name:
                    arcpy.management.DeleteField(output_data_path+"\Building_Property_Owner",Buil_Table_Field_N)

                    
            if checkbox_value:
                readme.write("\n")
                readme.write("\n10. PropertyOwner (tikili) ucun lazimi melumatlar export edildi")
            cursor.insertHtml('''<p><span style="color:green;">PropertyOwner (tikili) üçün lazımı məlumatlar export edildi. <br> </span>''')
            
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n10. PropertyOwner (tikili) cedveli export edile bilmedi. Araliq bazada olan Tikili tum layinin sutun adlarinin dogru olduguna diqqet edin!")
            cursor.insertHtml('''<p><span style="color:red;">PropertyOwner (tikili) cədvəli export edilə bilmədi. Aralıq bazada olan
                              Tikili tum layının sütun adlarının doğru olduğuna diqqət edin! <br> </span>''')
            
        if checkbox_value:    
            readme.close()

        ################################## Building Property Owner export ####################################


    def building_owner(self,output_data_path,checkbox_value,textBrowser,readme,head):
        ################################## Building Owner export ####################################
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor=textBrowser.textCursor()
        
        try:

            arcpy.conversion.ExportTable(output_data_path+"\BUILDING",output_data_path+"\Building_Owner")
            building_owner_fields = arcpy.ListFields(output_data_path+"\Building_Owner")

            require_Buil_Field_name = ["OBJECTID","FULL_NAME","DATE_OF_BIRTH","ID_CARD_NUMBER"]

            list_BUİL_PORPERTY_field = []

            for field in building_owner_fields:
                list_BUİL_PORPERTY_field.append(field.name)
                
            for Buil_Table_Field_N in list_BUİL_PORPERTY_field:
                if Buil_Table_Field_N not in require_Buil_Field_name:
                    arcpy.management.DeleteField(output_data_path+"\Building_Owner",Buil_Table_Field_N)

            if checkbox_value:
                readme.write("\n")
                readme.write("\n11. Owner (tikili) ucun lazimi melumatlar export edildi")
            cursor.insertHtml('''<p><span style="color:green;">Owner (tikili) üçün lazımı məlumatlar export edildi. <br> </span>''')
            
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n11. Owner (tikili) cedveli export edile bilmedi. Araliq bazada olan Tikili tum layinin sutun adlarinin dogru olduguna diqqet edin!")
            cursor.insertHtml('''<p><span style="color:red;">Owner (tikili) cədvəli export edilə bilmədi. Aralıq bazada olan
                              Tikili tum layının sütun adlarının doğru olduğuna diqqət edin! <br> </span>''')
            
        if checkbox_value:    
            readme.close()


        ################################## Building Owner export ####################################

    def building_delete_field(self,output_data_path,checkbox_value,textBrowser,readme,head):
        ################################## delete field ####################################
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor=textBrowser.textCursor()
        
        try:
        
            Building_Field = ["FK_BUILDING_NAME","BUILDING_NO","FK_CONSTRUCTION_MAT_TYPE","FK_ROOF_TYPE","FK_IS_INCOMPLETE","FK_HAS_HEATING",
                            "FK_HAS_GAS","FK_HAS_ELECTRICITY","FK_HAS_COLD_WATER","FK_HAS_WARM_WATER","FK_HAS_SEWAGE_WATER",
                            "FK_HAS_TELEPHONE","FLOOR_COUNT","ROOM_COUNT","BUILDING_AREA","REAL_AREA","DESCRIPTION","BUILDING_YEAR"]
                    
            building_fields = arcpy.ListFields(output_data_path+"\BUILDING")
            list_Building_field = []

            for field in building_fields:
                list_Building_field.append(field.name)


            for s in list_Building_field:
                if (s not in Building_Field) and (s!="OBJECTID" and s!="SHAPE" and s!="SHAPE_Length" and s!="SHAPE_Area"):
                    arcpy.management.DeleteField(output_data_path+"\BUILDING",s)

            if checkbox_value:
                readme.write("\n")
                readme.write("\n12. Buildingden lazimsiz sutunlar silindi")
            cursor.insertHtml('''<p><span style="color:green;">Building-dən lazımsız sütunlar silindi <br> </span>''')
            cursor.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------</strong> <br> </span>''')
            
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n12. Tikiliden lazimsiz sutunlar siline bilmedi. Neticlerin gonderildiyi bazanin movcud olduguna ve ya basqa proqram terefinden istifade edilmediyinden emin olun")
            cursor.insertHtml('''<p><span style="color:red;">Tikildən lazımsız sütunlar silinə bilmədi. Nəticələrin
                              göndərildiyi bazanın mövcdu olduğundan və ya bazanın başqa proqram tərəfindən məşğul edilmədiyindən
                              əmin olun<br> </span>''')
        
        if checkbox_value:    
            readme.close()

        ################################## delete field ####################################
    
        
        



    

