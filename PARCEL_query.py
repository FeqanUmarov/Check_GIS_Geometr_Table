import arcpy




################################## query ###################################
class Parcel:
    
    def __init__(self,base_data_path,uqodiya_data_base,output_data_path,checkbox_value,textBrowser,readme,head):
        super().__init__()
        base_data_path = base_data_path + '\RAYON'
        uqodiya_data_base = uqodiya_data_base + '\Alt_ugodyaa'
        self.write_field(base_data_path,output_data_path,uqodiya_data_base,checkbox_value,textBrowser,readme)
        self.export_PropertyGroup(output_data_path,checkbox_value,textBrowser,readme,head)
        self.export_Certifitacte(output_data_path,checkbox_value,textBrowser,readme,head)
        self.export_PropertyOwner(output_data_path,checkbox_value,textBrowser,readme,head)
        self.export_Owner(output_data_path,checkbox_value,textBrowser,readme,head)
        self.delete_Field(output_data_path,checkbox_value,textBrowser,readme,head)
        
    
    def write_field(self,base_data_path,output_data_path,uqodiya_data_base,checkbox_value,textBrowser,readme):
        cursor=textBrowser.textCursor()
        
        fields = {'FK_LANDUSAGE_TYPE':'!T_KATEGORI!','FK_BORDER_TYPE':'!SERHED_TIP!',
                        'REAL_AREA':'round(!SHAPE_Area!,0)','DESCRIPTION':'!ACIKLAMA!','FK_PARCEL_GROUNDS':'!Alt_ugodyaa.AZCAD_CODE!',
                        'FK_PROPERTY_TYPE':'!EMLAK_NOVU!','FK_OWNERSHIP_TYPE':'!MULKFORM!',
                        'FK_BALANCE_KEEPER':'!BALANS_SAKLAYICI!','TOTAL_AREA':'!SAHE!','ADDRESS':'!KEND_ADI!',
                        'FK_IS_LEGAL':'!LEQAL_MI!','REG_NO_OF_STATE_PROPERTY':'!DOVLET_REGISTR_NO!',
                        'CERTIFICATION_DATE':'!SENED_TARIXI!','CERTIFICATION_NO':'!SENEDNO!','FK_CERTIFICATION_TYPE':'!SENEDNOVU!',
                        'FILE_PATH':'!SENEDSEKIL!','DURATON_OF_USE':'!ISTIFADE_MUDDETI!','FULL_NAME':'!FULL_NAME!',
                        'DATE_OF_BIRTH':'!DOGUM_TARIXI!','ID_CARD_NUMBER':'!VESIKA_NOMRESI!','REGISTER_NO':'!REYESTR_NO!',
                        'FK_RIGHT_TYPE':'!ISTIFADE!'}
        try:
            arcpy.management.CopyFeatures(base_data_path+'\TORPAQ_TUM',output_data_path+"\PARCEL")

            for key,value in fields.items():

                if (key == "FK_BORDER_TYPE" or key == "FK_PROPERTY_TYPE" or
                    key == "FK_OWNERSHIP_TYPE" or key == "FK_IS_LEGAL" or key == "FK_LANDUSAGE_TYPE" or key == "FK_RIGHT_TYPE"):
                    arcpy.management.AddField(output_data_path+"\PARCEL",key, 'SHORT')
                    arcpy.management.CalculateField(output_data_path+"\PARCEL", key ,value, 'PYTHON3')

                elif (key == "FK_BALANCE_KEEPER" or key == "FK_CERTIFICATION_TYPE"):
                    arcpy.management.AddField(output_data_path+"\PARCEL",key, 'LONG')
                    arcpy.management.CalculateField(output_data_path+"\PARCEL", key ,value, 'PYTHON3')

                elif (key == "REAL_AREA" or key == "TOTAL_AREA"):
                    arcpy.management.AddField(output_data_path+"\PARCEL",key, 'DOUBLE')
                    arcpy.management.CalculateField(output_data_path+"\PARCEL", key ,value, 'PYTHON3')

                elif key == "FK_PARCEL_GROUNDS":
                    arcpy.management.AddField(output_data_path+"\PARCEL",key, 'SHORT')
                    arcpy.management.MakeFeatureLayer(output_data_path+"\PARCEL","make_join")
                    arcpy.management.AddJoin("make_join", 'ALT_IST_NOVU', uqodiya_data_base, 'ipad_kod')
                    arcpy.management.CalculateField("make_join", key ,value, 'PYTHON3')
                    arcpy.management.RemoveJoin("make_join", 'Alt_ugodyaa')

                elif key == "DATE_OF_BIRTH" or key == "CERTIFICATION_DATE":
                    arcpy.management.AddField(output_data_path+"\PARCEL",key, 'DATE')
                    arcpy.management.CalculateField(output_data_path+"\PARCEL", key ,value, 'PYTHON3')
                        
                else:
                    arcpy.management.AddField(output_data_path+"\PARCEL",key, 'TEXT')
                    arcpy.management.CalculateField(output_data_path+"\PARCEL", key ,value, 'PYTHON3')
                    
            if checkbox_value:
               
                readme.write("1. Torpaqda yeni sutunlar yaradildi ve kohne sutunlarda olan melumatlar kocuruldu")
            cursor.insertHtml('''<p><span style="color:green;">Torpaqda yeni sütunlar yaradıldı və köhnə sütunlarda olan məlumatlar
                                  köçürüldü. <br> </span>''')

                        
                        
                ################################## query ####################################
               
        except:
            if checkbox_value:
                
                readme.write("1. Torpaqda yeni sutunlarin yaradilmasinda ve melumatlarin yaradilmasinda xeta bas verdi. Araliq bazadaki sutun adlarina ve tiplerine nezer yetirin!")
            cursor.insertHtml('''<p><span style="color:red;">Torpaqda yeni sütunların yaradılmasında və məlumanların yazılmasında xəta baş verdi.
                                  Aralıq bazadakı sütun adlarına və tiplərinə nəzər yetirin! <br> </span>''')
        if checkbox_value:    
            readme.close()
            
            
        print("Oqrxdugun yerde xeta olmadi")
        
        

    def export_PropertyGroup(self,output_data_path,checkbox_value,textBrowser,readme,head):
        ################################## Parcel property export ####################################
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor=textBrowser.textCursor()
        try:

            arcpy.conversion.ExportTable(output_data_path+"\PARCEL",output_data_path+"\PARCEL_Property")
            parcel_property_fields = arcpy.ListFields(output_data_path+"\PARCEL_Property")

            require_Par_Field_name = ["OBJECTID","REGISTER_NO","FK_PROPERTY_TYPE","FK_OWNERSHIP_TYPE","FK_BALANCE_KEEPER","TOTAL_AREA",
                                    "ADDRESS","DESCRIPTION","FK_IS_LEGAL","REG_NO_OF_STATE_PROPERTY"]

            list_PARCEL_PORPERTY_field = []

            for field in parcel_property_fields:
                list_PARCEL_PORPERTY_field.append(field.name)
                
            for Par_Table_Field_N in list_PARCEL_PORPERTY_field:
                if Par_Table_Field_N not in require_Par_Field_name:
                    arcpy.management.DeleteField(output_data_path+"\PARCEL_Property",Par_Table_Field_N)
                    
                    
            if checkbox_value:
                readme.write("\n")
                readme.write("\n2. Property Group ucun lazimi melumatlar export edildi")
            cursor.insertHtml('''<p><span style="color:green;">Property group üçün lazımı məlumatlar export edildi. <br> </span>''')
                    
        
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n2. Property Group cedveli export edile bilmedi. Araliq bazada olan Torpaq tum layinin sutun adlarinin dogru olduguna diqqet edin!")
            cursor.insertHtml('''<p><span style="color:red;">Property Group cədvəli export edilə bilmədi. Aralıq bazada olan
                              Torpaq tum layının sütun adlarının doğru olduğuna diqqət edin! <br> </span>''')
        if checkbox_value:     
            readme.close()
            
        


        ################################## Parcel property export ####################################

    def export_Certifitacte(self,output_data_path,checkbox_value,textBrowser,readme,head):
        ################################## Parcel Certificate export ####################################
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor=textBrowser.textCursor()
        try:
                
            arcpy.conversion.ExportTable(output_data_path+"\PARCEL",output_data_path+"\PARCEL_Certificate")
            parcel_property_fields = arcpy.ListFields(output_data_path+"\PARCEL_Certificate")

            require_Par_Field_name = ["OBJECTID","CERTIFICATION_DATE","CERTIFICATION_NO","FK_CERTIFICATION_TYPE",
                                    "FILE_PATH","DURATON_OF_USE"]

            list_PARCEL_Certificate_field = []

            for field in parcel_property_fields:
                list_PARCEL_Certificate_field.append(field.name)
                
            for Par_Table_Field_N in list_PARCEL_Certificate_field:
                if Par_Table_Field_N not in require_Par_Field_name:
                    arcpy.management.DeleteField(output_data_path+"\PARCEL_Certificate",Par_Table_Field_N)
                    
                    
            if checkbox_value:
                readme.write("\n")
                readme.write("\n3. Certificate ucun lazimi melumatlar export edildi")
            cursor.insertHtml('''<p><span style="color:green;">Certificate üçün lazımı məlumatlar export edildi. <br> </span>''')

          
            
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n3. Certificate cedveli export edile bilmedi. Araliq bazada olan Torpaq tum layinin sutun adlarinin dogru olduguna diqqet edin!")
            cursor.insertHtml('''<p><span style="color:red;">Certificate cədvəli export edilə bilmədi. Aralıq bazada olan
                              Torpaq tum layının sütun adlarının doğru olduğuna diqqət edin! <br> </span>''')
        if checkbox_value:     
            readme.close()

        ################################## Parcel Certificate export ####################################


    def export_PropertyOwner(self,output_data_path,checkbox_value,textBrowser,readme,head):
        ################################## Parcel Property Owner export ####################################
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor=textBrowser.textCursor()
        try:

            arcpy.conversion.ExportTable(output_data_path+"\PARCEL",output_data_path+"\PARCEL_Property_Owner")
            parcel_property_fields = arcpy.ListFields(output_data_path+"\PARCEL_Property_Owner")

            require_Par_Field_name = ["OBJECTID","FK_RIGHT_TYPE"]

            list_PARCEL_Certificate_field = []

            for field in parcel_property_fields:
                list_PARCEL_Certificate_field.append(field.name)
                
            for Par_Table_Field_N in list_PARCEL_Certificate_field:
                if Par_Table_Field_N not in require_Par_Field_name:
                    arcpy.management.DeleteField(output_data_path+"\PARCEL_Property_Owner",Par_Table_Field_N)

                    
            if checkbox_value:
                readme.write("\n")
                readme.write("\n4. PropertyOwner ucun lazimi melumatlar export edildi")
            cursor.insertHtml('''<p><span style="color:green;">PropertyOwner üçün lazımı məlumatlar export edildi. <br> </span>''')
            
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n4. PropertyOwner cedveli export edile bilmedi. Araliq bazada olan Torpaq tum layinin sutun adlarinin dogru olduguna diqqet edin!")
            cursor.insertHtml('''<p><span style="color:red;">PropertyOwner cədvəli export edilə bilmədi. Aralıq bazada olan
                              Torpaq tum layının sütun adlarının doğru olduğuna diqqət edin! <br> </span>''')
        if checkbox_value:     
            readme.close()
            

        ################################## Parcel Property Owner export ####################################
        
        
    def export_Owner(self,output_data_path,checkbox_value,textBrowser,readme,head):

        ################################## Parcel Owner export ####################################
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor=textBrowser.textCursor()
        try:
            

            arcpy.conversion.ExportTable(output_data_path+"\PARCEL",output_data_path+"\PARCEL_Owner")
            parcel_property_fields = arcpy.ListFields(output_data_path+"\PARCEL_Owner")

            require_Par_Field_name = ["OBJECTID","FULL_NAME","DATE_OF_BIRTH","ID_CARD_NUMBER"]

            list_PARCEL_Certificate_field = []

            for field in parcel_property_fields:
                list_PARCEL_Certificate_field.append(field.name)
                
            for Par_Table_Field_N in list_PARCEL_Certificate_field:
                if Par_Table_Field_N not in require_Par_Field_name:
                    arcpy.management.DeleteField(output_data_path+"\PARCEL_Owner",Par_Table_Field_N)

            if checkbox_value:
                readme.write("\n")
                readme.write("\n5. Owner ucun lazimi melumatlar export edildi")
            cursor.insertHtml('''<p><span style="color:green;">Owner üçün lazımı məlumatlar export edildi. <br> </span>''')
            
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n5. Owner cedveli export edile bilmedi. Araliq bazada olan Torpaq tum layinin sutun adlarinin dogru olduguna diqqet edin!")
            cursor.insertHtml('''<p><span style="color:red;">Owner cədvəli export edilə bilmədi. Aralıq bazada olan
                              Torpaq tum layının sütun adlarının doğru olduğuna diqqət edin! <br> </span>''')
            
        if checkbox_value: 
            readme.close()
            


        ################################## Parcel Owner export ####################################


    def delete_Field(self,output_data_path,checkbox_value,textBrowser,readme,head):

        ################################## delete field Parcel ####################################
        if checkbox_value:
            readme = open(head+"\\Readme.txt","a+")
        cursor=textBrowser.textCursor()
        try:
                    
            parcel_fields = arcpy.ListFields(output_data_path+"\PARCEL")
            list_PARCEL_field = []

            for field in parcel_fields:
                list_PARCEL_field.append(field.name)


            for s in list_PARCEL_field:
                if (s!="FK_BORDER_TYPE" and s!="FK_LANDUSAGE_TYPE" and s!="FK_PARCEL_GROUNDS" and
                    s!="REAL_AREA" and s!="DESCRIPTION" and s!="FK_PROPERTY_GROUP") and (s!="OBJECTID" and s!="SHAPE" and s!="SHAPE_Length" and s!="SHAPE_Area"):
                    arcpy.management.DeleteField(output_data_path+"\PARCEL",s)

            if checkbox_value:
                readme.write("\n")
                readme.write("\n6. Parcelden lazimsiz sutunlar silindi")
            cursor.insertHtml('''<p><span style="color:green;">Parcel-dən lazımsız sütunlar silindi. <br> </span>''')
            cursor.insertHtml('''<p><span style="color:black;"><strong>-----------------------------------------------------------</strong><br> </span>''')
            
        except:
            if checkbox_value:
                readme.write("\n")
                readme.write("\n6. Parcelden lazimsiz sutunlar siline bilmedi. Neticlerin gonderildiyi bazanin movcud olduguna ve ya basqa proqram terefinden istifade edilmediyinden emin olun")
            cursor.insertHtml('''<p><span style="color:red;">Parceldən lazımsız sütunlar silinə bilmədi. Nəticələrin
                              göndərildiyi bazanın mövcdu olduğundan və ya bazanın başqa proqram tərəfindən məşğul edilmədiyindən
                              əmin olun. <br> </span>''')
            
        if checkbox_value:     
            readme.close()
            
            

        ################################## delete field Parcel ####################################
        
        
    