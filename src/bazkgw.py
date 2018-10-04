import os, sys, time
from util import *

def kimotogravitywell(blockindex, targetblocksspacingseconds, pastblocksmin, pastblocksmax):

        debug                      = False
        startrecord                = len(blockindex)
	blocklastsolved	           = startrecord
	blockreading	           = startrecord
	pastblocksmass             = float(0)
	pastrateactualseconds      = float(0)
	pastratetargetseconds      = float(0)
	pastrateadjustmentratio    = float(1)
	pastdifficultyaverage      = float(0)
	pastdifficultyaverageprev  = float(0)
	eventhorizondeviation      = float(0)
	eventhorizondeviationfast  = float(0)
	eventhorizondeviationslow  = float(0)
	bnproofofworklimit         = 0x1e00ffff

        diffiter = 0
	while True:
                
                if debug is True:
                   print 'diffiter ' + str(diffiter)

		diffiter += 1	
		if (pastblocksmax > 0 and diffiter > pastblocksmax):
		    break
		pastblocksmass += 1

		if (diffiter == 1):			    
		  pastdifficultyaverage = getfromblockindex(blocklastsolved, 1, blockindex)
		else:
                  #note: this avoids a 'negative shift' exception from python
                  try:
		     pastdifficultyaverage = ((getfromblockindex(blocklastsolved, 1, blockindex) - \
                                             pastdifficultyaverageprev) / diffiter) + pastdifficultyaverageprev
                  except:
                     if debug is True:
                        print 'hit exception.. continuing'
                     break

		pastdifficultyaverageprev = pastdifficultyaverage
		pastrateactualseconds    = int(getfromblockindex(blocklastsolved, 0, blockindex)) - \
                                           int(getfromblockindex(blockreading, 0, blockindex))
		pastratetargetseconds    = 30 * pastblocksmass
		pastrateadjustmentratio  = float(1)		
		if pastrateactualseconds < 0:
		   pastrateactualseconds = 0
		if pastrateactualseconds != 0 and pastratetargetseconds != 0:
		   pastrateadjustmentratio = float(pastratetargetseconds) / float(pastrateactualseconds)
		eventhorizondeviation    = 1 + ( 0.7084 * ((pastblocksmass / 144) ** -1.228))
		eventhorizondeviationfast = eventhorizondeviation
		eventhorizondeviationslow = 1 / eventhorizondeviation
		blockreading -= 1

	return (pastdifficultyaverage)

def getnextworkrequired(blockindex):

    blockstargetspacing  = 30
    pastblocksmin        = 28.8
    pastblocksmax        = 403.2
    newbits = kimotogravitywell(blockindex, blockstargetspacing, pastblocksmin, pastblocksmax)
    return newbits

def getfromblockindex(count, type, blockindex):

    #print 'complete blockindex [' + str(blockindex) + ']'
    print 'asked for count = ' + str(count),
    print 'of type = ' + str(type)

    retrieved = ''
    try:
      for num in blockindex:
          if 'BLK' + str(count) in num:
             retrieved = num.replace('BLK' + str(count) + ',','')
             break
    except:
      print 'blockindex error'
    if len(retrieved) > 0:
       return retrieved.split(',')[type]
    else:
       return 'not found'