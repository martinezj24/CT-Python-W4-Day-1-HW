def mood_response(mood):
    if mood.lower() == 'happy' or mood.lower() == 'excited':
        return '"I know that nothing is better for them than to rejoice, and to do good in their lives" Ecc. 3:12'
    elif mood.lower() == 'sad' or mood.lower() == 'upset':
        return '"The righteous cry out, and the LORD hears, and delivers them out of all of their troubles" Ps. 34:17'
    elif mood.lower() == 'mad' or mood.lower() == 'angry':
        return '"If you forgive those who sin against you, your heavenly Father will forgive you." Matt. 6:14'
    elif mood.lower() == 'anxious' or mood.lower() == 'worried':
        return '''"Do not worry about these things, saying What will we eat? What will we drink? What will we wear? These things dominate the thoughts of unbelievers,
            but your heavenly Father already knows all your needs. Seek first the Kingdom of God above all else, and live righteously, and he will give you 
                everything you need. So dont worry about tomorrow, for tomorrow will bring its own worries. 
                    Todays trouble is enough for today" Matt. 6:31-34'''
    elif mood.lower() == 'fear' or mood.lower() == 'afraid':
        return '"Have I not commanded you? Be strong courageous! Do not be afraid or discouraged, for the LORD your God is with you wherever you go." Josh. 1:9'
    elif mood.lower() == 'tired' or mood.lower() == 'exhausted':
        return '''"The LORD is my shepard; I shall not want. He makes me lie down in green pastures; He leads me besides the still waters.
                   He restores my soul; He leads me in the paths of righteousness For His name's sake." Ps. 23: 1-2'''
    elif mood.lower() == 'moody' or mood.lower() == 'annoyed':
        return '''"Let all bitterness, wrath, anger, clamor, and evil speaking be put away from you, with all malice.
                   And be kind to one another, tenderhearted, forgiving one another, even as God in Christ forgave you." Ephs. 4:31-32'''
    else:
        return 'Invalid entry. Try again'
            