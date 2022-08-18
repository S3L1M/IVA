#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.1),
    on August 18, 2022, at 09:54
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.1'
expName = 'iva'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'stimulus size': '8.5',
    'start spatial freq': '0.8',
    'end spatial freq': '25.6',
    'stimulus duration': '1',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\mohamedselim\\Desktop\\GSoC\\IVA\\iva_stair_2.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=True,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "grating_acuity" ---
# Set experiment start values for variable component pos_list
pos_list = {'right':(16,0), 'left':(-16,0), 'top-right':(16,7), 'top-left':(-16, 7), 'bottom-right':(16,-7), 'bottom-left':(-16, -7)}
pos_listContainer = []
# Set experiment start values for variable component position
position = (0, 0)
positionContainer = []
GA = visual.GratingStim(
    win=win, name='GA',units='deg', 
    tex='sqr', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=(float(expInfo['stimulus size']), float(expInfo['stimulus size'])), sf=1.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=1.0, blendmode='avg',
    texRes=512.0, interpolate=True, depth=-2.0)
aperture = visual.Aperture(
    win=win, name='aperture',
    units='deg', size=[float(expInfo['stimulus size'])], pos=[0,0], ori=0.0,
    shape='circle', anchor='center'
)
aperture.disable()  # disable until its actually used
# Set experiment start values for variable component spatial_freq
spatial_freq = float(expInfo['start spatial freq'])
spatial_freqContainer = []
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "central_fixation" ---
placeholder = visual.TextStim(win=win, name='placeholder',
    text='Central fixation\nPlace Holder',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --------Prepare to start Staircase "GA_loop" --------
# set up handler to look after next chosen value etc
GA_loop = data.StairHandler(startVal=float(expInfo['start spatial freq']), extraInfo=expInfo,
    stepSizes=[-0.8,-0.8,-0.4,-0.4,-0.2], stepType='lin',
    nReversals=0.0, nTrials=12.0, 
    nUp=1.0, nDown=2.0,
    minVal=float(expInfo['start spatial freq']), maxVal=float(expInfo['end spatial freq']),
    originPath=-1, name='GA_loop')
thisExp.addLoop(GA_loop)  # add the loop to the experiment
level = thisGA_loop = float(expInfo['start spatial freq'])  # initialise some vals

for thisGA_loop in GA_loop:
    currentLoop = GA_loop
    level = thisGA_loop
    
    # --- Prepare to start Routine "grating_acuity" ---
    continueRoutine = True
    # update component parameters for each repeat
    position = (randchoice([-1, 1])*16, 0)  # Set routine start values for position
    GA.setPos(position)
    GA.setSF(level if level>float(expInfo['start spatial freq']) else float(expInfo['start spatial freq']))
    aperture.setPos(position)
    spatial_freq = level  # Set routine start values for spatial_freq
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # Run 'Begin Routine' code from set_answer
    correctAns = 'right' if pos_list['right'] == position else 'left'
    # keep track of which components have finished
    grating_acuityComponents = [GA, aperture, key_resp]
    for thisComponent in grating_acuityComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "grating_acuity" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *GA* updates
        if GA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            GA.frameNStart = frameN  # exact frame index
            GA.tStart = t  # local t and not account for scr refresh
            GA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(GA, 'tStartRefresh')  # time at next scr refresh
            GA.setAutoDraw(True)
        if GA.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > GA.tStartRefresh + float(expInfo["stimulus duration"])-frameTolerance:
                # keep track of stop time/frame for later
                GA.tStop = t  # not accounting for scr refresh
                GA.frameNStop = frameN  # exact frame index
                GA.setAutoDraw(False)
        
# *aperture* updates
        if aperture.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            aperture.frameNStart = frameN  # exact frame index
            aperture.tStart = t  # local t and not account for scr refresh
            aperture.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(aperture, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'aperture.started')
            aperture.enabled = True
        if aperture.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > aperture.tStartRefresh + float(expInfo["stimulus duration"])-frameTolerance:
                # keep track of stop time/frame for later
                aperture.tStop = t  # not accounting for scr refresh
                aperture.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'aperture.stopped')
                aperture.enabled = False
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + float(expInfo["stimulus duration"])-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.stopped')
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left','right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(correctAns)) or (key_resp.keys == correctAns):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in grating_acuityComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "grating_acuity" ---
    for thisComponent in grating_acuityComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('position.routineEndVal', position)  # Save end routine value
    aperture.enabled = False  # just in case it was left enabled
    thisExp.addData('spatial_freq.routineEndVal', spatial_freq)  # Save end routine value
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for GA_loop (StairHandler)
    GA_loop.addResponse(key_resp.corr, level)
    GA_loop.addOtherData('key_resp.rt', key_resp.rt)
    # the Routine "grating_acuity" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "central_fixation" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    central_fixationComponents = [placeholder]
    for thisComponent in central_fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "central_fixation" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *placeholder* updates
        if placeholder.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            placeholder.frameNStart = frameN  # exact frame index
            placeholder.tStart = t  # local t and not account for scr refresh
            placeholder.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(placeholder, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'placeholder.started')
            placeholder.setAutoDraw(True)
        if placeholder.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > placeholder.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                placeholder.tStop = t  # not accounting for scr refresh
                placeholder.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'placeholder.stopped')
                placeholder.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in central_fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "central_fixation" ---
    for thisComponent in central_fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine
    routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
# staircase completed


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
