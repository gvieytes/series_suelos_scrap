import os

def doc_to_text_catdoc(filename):
    (fi, fo, fe) = os.popen3('catdoc -w "%s"' % filename)
    fi.close()
    retval = fo.read()
    erroroutput = fe.read()
    fo.close()
    fe.close()
    if not erroroutput:
        return retval
    else:
        raise OSError("Executing the command caused an error: %s" % erroroutput)



infile = 'unidades_cartograficas_50000.doc'

print(doc_to_text_catdoc(infile))
