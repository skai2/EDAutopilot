def reposition(refueled_multiplier=1):
    logging.debug('position')
    scan = get_scanner()
    if scan == 1:
        logging.debug('position=scanning')
        send(keys['PrimaryFire'], state=1)
    elif scan == 2:
        logging.debug('position=scanning')
        send(keys['SecondaryFire'], state=1)
    send(keys['PitchUpButton'], state=1)
    sleep(5)
    send(keys['PitchUpButton'], state=0)
    send(keys['SetSpeed100'])
    send(keys['PitchUpButton'], state=1)
    while sun_percent() > 3:
        sleep(1)
    sleep(5)
    send(keys['PitchUpButton'], state=0)
    sleep(5*refueled_multiplier)
    if scan == 1:
        logging.debug('position=scanning complete')
        send(keys['PrimaryFire'], state=0)
    elif scan == 2:
        logging.debug('position=scanning complete')
        send(keys['SecondaryFire'], state=0)
    logging.debug('position=complete')
    return True