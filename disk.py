def keep_log(name, score, date):
    with open('score_log.txt', 'a') as history:
        history.write('\n{} | {} | {}'.format(name, score, date))