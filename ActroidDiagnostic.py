#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file ActroidDiagnostic.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist
import Tkinter as tk
import JointFrame
#JointFrameの中のtestを呼び出す。

frames = []


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">

my_tuple = (("1:Eyebrows up&down  ",0,255),
            ("2:Eyelids open&shut ",0,255),
            ("3:Eyes right&left   ",0,255),
            ("4:Eyes up&down      ",0,255),
            ("5:Mouth open&shut   ",0,255),
            ("6:left neck         ",0,255),
            ("7:right neck        ",0,255),
            ("8:Neck turning      ",0,255),
            ("9:left arm up       ",0,255),
            ("10:left arm open    ",0,255),
            ("11:left upper arm   ",0,255),
            ("12:left elbow       ",0,255),
            ("13:left forearm     ",0,255),
            ("14:left hand length ",0,255),
            ("15:left hand side   ",0,255),
            ("16:right arm up     ",0,255),
            ("17:right arm open   ",0,255),
            ("18:right upper arm  ",0,255),
            ("19:right elbow      ",0,255),
            ("20:right forearm    ",0,255),
            ("21:right hand length",0,255),
            ("22:right hand side  ",0,255),
            ("23:Body front&back  ",0,255),
            ("24:Body turning     ",0,255))


actroiddiagnostic_spec = ["implementation_id", "ActroidDiagnostic", 
		 "type_name",         "ActroidDiagnostic", 
		 "description",       "ModuleDescription", 
		 "version",           "1.0.0", 
		 "vendor",            "VenderName", 
		 "category",          "Category", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class ActroidDiagnostic
# @brief ModuleDescription
# 
# 
class ActroidDiagnostic(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_position = RTC.TimedDoubleSeq(RTC.Time(0,0),[])
		"""
		"""
		self._positionIn = OpenRTM_aist.InPort("position", self._d_position)
		self._d_purpose = RTC.TimedDoubleSeq(RTC.Time(0,0),[])
		"""
		"""
		self._purposeOut = OpenRTM_aist.OutPort("purpose", self._d_purpose)


		


		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		
		# Set InPort buffers
		self.addInPort("position",self._positionIn)
		
		# Set OutPort buffers
		self.addOutPort("purpose",self._purposeOut)
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The shutdown action when ExecutionContext stop
		# former rtc_stopping_entry()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onShutdown(self, ec_id):
	
		return RTC.RTC_OK
	
		##
		#
		# The activated action (Active state entry action)
		# former rtc_active_entry()
		#
		# @param ec_id target ExecutionContext Id
		# 
		# @return RTC::ReturnCode_t
		#
		#
	def onActivated(self, ec_id):
	
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The deactivated action (Active state exit action)
	#	# former rtc_active_exit()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onDeactivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
		##
		#
		# The execution action that is invoked periodically
		# former rtc_active_do()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onExecute(self, ec_id):
                print 'onExecute start'

                data_array = []
                data_array2 = []
                try:
                        global frames
                        #print frames[0].getvalue()
                        #frames[0].setvalue(str(frames[0].getvalue()))
                        #self._purposeOut.write()
                        #time.sleep(0.01)
                        #return RTC.RTC_OK
                
        
                        #global frames
                        for num in range(0, 24):
                                value = frames[num].getvalue()
                                #value = 1
                                #data_array = [[]]*24
                                data_array.append(value)
                                #data_array[data_array].append(data_array)
                                #print str(frames[value]) , str(frames[value].getvalue())
                                #frames[value].setvalue(frames[value].getvalue())
                                #self._purposeOut.write()
                                #time.sleep(0.01)
                                #return RTC.RTC_OK
                        self._d_purpose.data = data_array
                        print self._d_purpose
                        self._purposeOut.write()
                
                        if self._positionIn.isNew():
                                indata = self._positionIn.read()
                                print "Receive %d datas" % len(indata.data)
                                for v in indata.data:
                                        print "Data is %d" % (v)
                                for n in range(0, 24):
                                        val = frames[n].getvalue()
                                        frames[n].setvalue(val)
                                
                        #time.sleep(0.01)
                        return RTC.RTC_OK
                
                except Exception, e:
                        print 'Exception : ', e
                        pass
                #except IOError as err:
                #        print("I/O error: {0}".format(err))
                #except ValueError:
                #        print("データが整数に変換できません")
                #except:
                #        print("予期せぬエラー：", sys.exc_info()[0])
                #        raise #例外の再検出
                return RTC.RTC_OK
	
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def ActroidDiagnosticInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=actroiddiagnostic_spec)
    manager.registerFactory(profile,
                            ActroidDiagnostic,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    ActroidDiagnosticInit(manager)

    # Create a component
    comp = manager.createComponent("ActroidDiagnostic")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager(True)
	
        global  frames
        root, frames = JointFrame.test()

        for num in range(0, 24):
                print "scale value is ", str(frames[num].getvalue())
        
	root.mainloop()

	

if __name__ == "__main__":
	main()

