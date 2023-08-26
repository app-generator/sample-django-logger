from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

import os, sys
from inspect import currentframe, getframeinfo
from logger import *

def index(request):

    func_name  = sys._getframe().f_code.co_name
    logger( f'[{__name__}->{func_name}(), L:{currentframe().f_lineno}] ' + 'My LOG Message (default LEVEL)' )

    logger_info( f'[{__name__}->{func_name}(), L:{currentframe().f_lineno}] ' + 'INFO Message' )

    logger_error( f'[{__name__}->{func_name}(), L:{currentframe().f_lineno}] ' + 'ERROR Message' )

    logger_critical( f'[{__name__}->{func_name}(), L:{currentframe().f_lineno}] ' + 'CRITICAL Message' )

    # Page from the theme 
    return render(request, 'pages/index.html')
