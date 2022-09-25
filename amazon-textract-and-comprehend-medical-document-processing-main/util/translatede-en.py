#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 20:56:00 2022

@author: thilani
"""
# translate the text from de to en
translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)

result = translate.translate_text(Text=full_text[:5000], SourceLanguageCode="de", TargetLanguageCode="en")
enFullText = result.get('TranslatedText')
print('TranslatedText: ' + enFullText)
