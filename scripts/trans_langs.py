﻿# List of languages we support, their iso codes and id as understood
# by Windows SDK (LANG_* and SUBLANG_*_*).
# See http://msdn.microsoft.com/en-us/library/dd318693.aspx for the full list.
g_langs = [
    ('af', 'Afrikaans', '_LANGID(LANG_AFRIKAANS)'),
    ('am', 'Armenian (Հայերեն)', '_LANGID(LANG_ARMENIAN)'),
    ('ar', 'Arabic (الْعَرَبيّة)', '_LANGID(LANG_ARABIC)', 'RTL'),
    ('az', 'Azerbaijani (Azərbaycanca)', '_LANGID(LANG_AZERI)'),
    ('bg', 'Bulgarian (Български)', '_LANGID(LANG_BULGARIAN)'),
    ('bn', 'Bengali (বাংলা)', '_LANGID(LANG_BENGALI)'),
    {'co', 'Corsican', '_LANGID(LANG_CORSICAN)'},
    ('br', 'Portuguese - Brazil (Português)', 'MAKELANGID(LANG_PORTUGUESE, SUBLANG_PORTUGUESE_BRAZILIAN)'),
    ('bs', 'Bosnian (Bosanski)', 'MAKELANGID(LANG_BOSNIAN, SUBLANG_BOSNIAN_BOSNIA_HERZEGOVINA_LATIN)'),
    ('by', 'Belarusian (Беларуская)', '_LANGID(LANG_BELARUSIAN)'),
    ('ca', 'Catalan (Català)', '_LANGID(LANG_CATALAN)'),
    ('ca-xv', 'Catalan-Valencian (Català-Valencià)', '(LANGID)-1'),
    ('cn', 'Chinese Simplified (简体中文)', 'MAKELANGID(LANG_CHINESE, SUBLANG_CHINESE_SIMPLIFIED)'),
    ('cy', 'Welsh (Cymraeg)', '_LANGID(LANG_WELSH)'),
    ('cz', 'Czech (Čeština)', '_LANGID(LANG_CZECH)'),
    ('de', 'German (Deutsch)', '_LANGID(LANG_GERMAN)'),
    ('dk', 'Danish (Dansk)', '_LANGID(LANG_DANISH)'),
    ('el', 'Greek (Ελληνικά)', '_LANGID(LANG_GREEK)'),
    ('en', 'English', '_LANGID(LANG_ENGLISH)'),
    ('es', 'Spanish (Español)', '_LANGID(LANG_SPANISH)'),
    ('et', 'Estonian (Eesti)', '_LANGID(LANG_ESTONIAN)'),
    ('eu', 'Basque (Euskara)', '_LANGID(LANG_BASQUE)'),
    ('fa', 'Persian (فارسی)', '_LANGID(LANG_FARSI)', 'RTL'),
    ('fi', 'Finnish (Suomi)', '_LANGID(LANG_FINNISH)'),
    ('fr', 'French (Français)', '_LANGID(LANG_FRENCH)'),
    ('fy-nl', 'Frisian (Frysk)', '_LANGID(LANG_FRISIAN)'),
    ('ga', 'Irish (Gaeilge)', '_LANGID(LANG_IRISH)'),
    ('gl', 'Galician (Galego)', '_LANGID(LANG_GALICIAN)'),
    ('he', 'Hebrew (עברית)', '_LANGID(LANG_HEBREW)', 'RTL'),
    ('hi', 'Hindi (हिंदी)', '_LANGID(LANG_HINDI)'),
    ('hr', 'Croatian (Hrvatski)', '_LANGID(LANG_CROATIAN)'),
    ('hu', 'Hungarian (Magyar)', '_LANGID(LANG_HUNGARIAN)'),
    ('id', 'Indonesian (Bahasa Indonesia)', '_LANGID(LANG_INDONESIAN)'),
    ('it', 'Italian (Italiano)', '_LANGID(LANG_ITALIAN)'),
    ('ja', 'Japanese (日本語)', '_LANGID(LANG_JAPANESE)'),
    ('jv', 'Javanese (ꦧꦱꦗꦮ)', '(LANGID)-1'),
    ('ka', 'Georgian (ქართული)', '_LANGID(LANG_GEORGIAN)'),
    ('kr', 'Korean (한국어)', '_LANGID(LANG_KOREAN)'),
    ('ku', 'Kurdish (كوردی)', 'MAKELANGID(LANG_CENTRAL_KURDISH, SUBLANG_CENTRAL_KURDISH_CENTRAL_KURDISH_IRAQ)', 'RTL'),
    ('kw', 'Cornish (Kernewek)', '(LANGID)-1'),
    ('lt', 'Lithuanian (Lietuvių)', '_LANGID(LANG_LITHUANIAN)'),
    ('lv', 'Latvian (latviešu valoda)', '_LANGID(LANG_LATVIAN)'),
    ('mk', 'Macedonian (македонски)', '_LANGID(LANG_MACEDONIAN)'),
    ('ml', 'Malayalam (മലയാളം)', '_LANGID(LANG_MALAYALAM)'),
    ('mm', 'Burmese (ဗမာ စာ)', '(LANGID)-1'),
    ('my', 'Malaysian (Bahasa Melayu)', '_LANGID(LANG_MALAY)'),
    ('ne', 'Nepali (नेपाली)', '_LANGID(LANG_NEPALI)'),
    ('nl', 'Dutch (Nederlands)', '_LANGID(LANG_DUTCH)'),
    ('nn', 'Norwegian Neo-Norwegian (Norsk nynorsk)', 'MAKELANGID(LANG_NORWEGIAN, SUBLANG_NORWEGIAN_NYNORSK)'),
    ('no', 'Norwegian (Norsk)', 'MAKELANGID(LANG_NORWEGIAN, SUBLANG_NORWEGIAN_BOKMAL)'),
    ('pa', 'Punjabi (ਪੰਜਾਬੀ)', '_LANGID(LANG_PUNJABI)'),
    ('pl', 'Polish (Polski)', '_LANGID(LANG_POLISH)'),
    ('pt', 'Portuguese - Portugal (Português)', '_LANGID(LANG_PORTUGUESE)'),
    ('ro', 'Romanian (Română)', '_LANGID(LANG_ROMANIAN)'),
    ('ru', 'Russian (Русский)', '_LANGID(LANG_RUSSIAN)'),
    ('si', 'Sinhala (සිංහල)', '_LANGID(LANG_SINHALESE)'),
    ('sk', 'Slovak (Slovenčina)', '_LANGID(LANG_SLOVAK)'),
    ('sl', 'Slovenian (Slovenščina)', '_LANGID(LANG_SLOVENIAN)'),
    ('sn', 'Shona (Shona)', '(LANGID)-1'),
    ('sp-rs', 'Serbian (Latin)', 'MAKELANGID(LANG_SERBIAN, SUBLANG_SERBIAN_LATIN)'),
    ('sq', 'Albanian (Shqip)', '_LANGID(LANG_ALBANIAN)'),
    ('sr-rs', 'Serbian (Cyrillic)', 'MAKELANGID(LANG_SERBIAN, SUBLANG_SERBIAN_CYRILLIC)'),
    ('sv', 'Swedish (Svenska)', '_LANGID(LANG_SWEDISH)'),
    ('ta', 'Tamil (தமிழ்)', '_LANGID(LANG_TAMIL)'),
    ('th', 'Thai (ภาษาไทย)', '_LANGID(LANG_THAI)'),
    ('tl', 'Tagalog (Tagalog)', '_LANGID(LANG_FILIPINO)'),
    ('tr', 'Turkish (Türkçe)', '_LANGID(LANG_TURKISH)'),
    ('tw', 'Chinese Traditional (繁體中文)', 'MAKELANGID(LANG_CHINESE, SUBLANG_CHINESE_TRADITIONAL)'),
    ('uk', 'Ukrainian (Українська)', '_LANGID(LANG_UKRAINIAN)'),
    ('uz', 'Uzbek (O\'zbek)', '_LANGID(LANG_UZBEK)'),
    ('vn', 'Vietnamese (Việt Nam)', '_LANGID(LANG_VIETNAMESE)'),
]
