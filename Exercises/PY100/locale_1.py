def extract_language(locale):
    locale_language = locale.split('_')[0]
    return locale_language


def extract_region(locale):
    region = (locale.split('_')[1]).split('.')[0]
    return region

# print(extract_language('en_US.UTF-8'))      # en
# print(extract_language('en_GB.UTF-8'))      # en
# print(extract_language('ko_KR.UTF-16'))     # ko

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR