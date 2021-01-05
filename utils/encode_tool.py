# Base64 format contains characters like '+' and '/', but net url don't
# allow their appearance. Instead, url allows the safe_url_base64
# format and can automatically recognize the special converted
# characters in it.
def safe_url_base64(base64):
    return base64.replace('+', '-').replace('/', '_')


# Mysql database don't allow the appearance of '=' in data, so before
# saving it, '=' at the end of the string should be eliminated.
def db_parse(s):
    return s[:-1] if s[-1] == '=' else s


def concat_array(array):
    if array:
        res = array[0]
        for i in range(1, len(array)):
            res = '{}#{}'.format(res, array[i])
        return res
    return ''
