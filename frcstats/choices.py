from collections import OrderedDict


auton_def_choices = OrderedDict(
    [
        ('portc', 'portcullis'),
        ('cdf', 'cheval de frise'),
        ('moat', 'moat'),
        ('ramparts', 'ramparts'),
        ('drawb', 'drawbridge'),
        ('sallyp', 'sallyport'),
        ('rockwall', 'rock wall'),
        ('rought', 'rough terrain'),
        ('lowbar', 'low bar'),
        ('none', 'none')
    ]
)

teleop_def_choices = (
    (3, 'crossed twice'),
    (2, 'crossed once'),
    (4, 'did not cross'),
    (1, 'got stuck'),
    (0, 'not in play')
)

hang_options = (
    (2, 'yes'),
    (0, 'did not hang'),
    (1, 'attempted')
)

defense_options = (
    (1, 'yes'),
    (0, 'no')
)
