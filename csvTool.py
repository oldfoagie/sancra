from datetime import datetime
from adaptor.fields import *
from adaptor.model import CsvModel, CsvDbModel, ImproperlyConfigured,\
    CsvException, CsvDataException, TabularLayout, SkipRow,\
    GroupedCsvModel, CsvFieldDataException
from web.models import *



class CodeCSvModel(CsvModel):

    codeid = CharField()
    remotecode = CharField()
    active = BooleanField()
    created = DateField()
    modified = DateField()
    incentiveid = CharField()

    class Meta:
        delimiter = ";"
        dbModel = Code
