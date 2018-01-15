from logs import logDecorator as lD 
import json

config = json.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.plotWork'


@lD.log(logBase + '.readWorkData')
def readWorkData(logger):
    '''Reads the information form work
    
    This function simply reads the data and converts
    it into a dictionary that can later be used for 
    plotting.
    
    Decorators:
        lD.log
    
    Arguments:
        logger {[type]} -- [description]
    
    Returns:
        list -- returns a list of dictionaries containing 
            work information.
    '''
    data = {}

    try:
        data = json.load(open('../data/raw_data/timeline.json'))
        if 'work' in data:
            data = data['work']
        else:
            logger.error('Unable to find work information within the data')
            return []


    except Exception as e:
        logger.error('Unable to read work information: {}'.format(str(e)))
        return []

    return data


@lD.log(logBase + '.plotWork')
def plotWork(logger):
    '''print a line
    
    This function simply prints a single line
    
    Parameters
    ----------
    logger : {[type]}
        [description]
    '''

    workData = readWorkData()
    print(workData)

    return

@lD.log(logBase + '.main')
def main(logger):
    '''main function for module1
    
    This function finishes all the tasks for the
    main function. This is a way in which a 
    particular module is going to be executed. 
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger function
    '''

    plotWork()

    return

