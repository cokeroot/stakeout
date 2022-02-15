import pywin
import win32serviceutil
import socket
import servicemanager
import win32event
import win32service

class SMWinservice(win32serviceutil.ServiceFramework):
    #class for windows service
    _svc_name_ = 'SECRETSERVICE'
    _svc_display_name_ = 'SECRETSERVICE'
    _svc_description_ = 'dont worry about it'

    @classmethod
    def parse_cmd(cls):
        #parse cmd line
        win32serviceutil.HandleCommandLine(cls)
    
    def __init__(self, args):
        #construct winservice
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(60)
    def SvcStop(self):
        #stop service when required
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
    def SvcDoRun(self):
        #START SERVICE WHEN REQUESTED
        self.start()
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,servicemanager.PYS_SERVICE_STARTED,(self._svc_name_,''))
        self.main()
    
    def start(self):

        pass

    def stop(self):

        pass

    def main(self):
        
        pass
