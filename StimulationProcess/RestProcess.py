from EventController import EventController
from StimulationProcess.BasicStimulationProcess import BasicStimulationProcess
from psychopy import event, visual
import time

class RestProcess(BasicStimulationProcess):
    
    def __init__(self) -> None:
        super().__init__()
        

    def change(self):
        
        #rest --> prepare
        self.controller.current_process = self.controller.prepare_process
        
    
    def run(self):
    
        self.w.flip()
        text = '按空格键继续'
        prepare_finish_text=visual.TextStim(self.w, pos=[0, 0], text=text, color=(255, 255, 255),colorSpace='rgb255')
        prepare_finish_text.draw()
        self.w.flip()
        event.waitKeys(keyList=['space'])
        self.change()