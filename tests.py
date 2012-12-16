 # -*- coding: UTF-8 -*-
"""Unit test for roman.py"""

import ft
import unittest
import base64

"""13000+ Charaters from http://www.gutenberg.org/cache/epub/46/pg46.txt"""
longString = """Once upon a time--of all the good days in the year,
on Christmas Eve--old Scrooge sat busy in his
counting-house. It was cold, bleak, biting weather: foggy
withal: and he could hear the people in the court outside,
go wheezing up and down, beating their hands
upon their breasts, and stamping their feet upon the
pavement stones to warm them. The city clocks had
only just gone three, but it was quite dark already--
it had not been light all day--and candles were flaring
in the windows of the neighbouring offices, like
ruddy smears upon the palpable brown air. The fog
came pouring in at every chink and keyhole, and was
so dense without, that although the court was of the
narrowest, the houses opposite were mere phantoms.
To see the dingy cloud come drooping down, obscuring
everything, one might have thought that Nature
lived hard by, and was brewing on a large scale.

The door of Scrooge's counting-house was open
that he might keep his eye upon his clerk, who in a
dismal little cell beyond, a sort of tank, was copying
letters. Scrooge had a very small fire, but the clerk's
fire was so very much smaller that it looked like one
coal. But he couldn't replenish it, for Scrooge kept
the coal-box in his own room; and so surely as the
clerk came in with the shovel, the master predicted
that it would be necessary for them to part. Wherefore
the clerk put on his white comforter, and tried to
warm himself at the candle; in which effort, not being
a man of a strong imagination, he failed.

"A merry Christmas, uncle! God save you!" cried
a cheerful voice. It was the voice of Scrooge's
nephew, who came upon him so quickly that this was
the first intimation he had of his approach.

"Bah!" said Scrooge, "Humbug!"

He had so heated himself with rapid walking in the
fog and frost, this nephew of Scrooge's, that he was
all in a glow; his face was ruddy and handsome; his
eyes sparkled, and his breath smoked again.

"Christmas a humbug, uncle!" said Scrooge's
nephew. "You don't mean that, I am sure?"

"I do," said Scrooge. "Merry Christmas! What
right have you to be merry? What reason have you
to be merry? You're poor enough."

"Come, then," returned the nephew gaily. "What
right have you to be dismal? What reason have you
to be morose? You're rich enough."

Scrooge having no better answer ready on the spur
of the moment, said, "Bah!" again; and followed it up
with "Humbug."

"Don't be cross, uncle!" said the nephew.

"What else can I be," returned the uncle, "when I
live in such a world of fools as this? Merry Christmas!
Out upon merry Christmas! What's Christmas
time to you but a time for paying bills without
money; a time for finding yourself a year older, but
not an hour richer; a time for balancing your books
and having every item in 'em through a round dozen
of months presented dead against you? If I could
work my will," said Scrooge indignantly, "every idiot
who goes about with 'Merry Christmas' on his lips,
should be boiled with his own pudding, and buried
with a stake of holly through his heart. He should!"

"Uncle!" pleaded the nephew.

"Nephew!" returned the uncle sternly, "keep Christmas
in your own way, and let me keep it in mine."

"Keep it!" repeated Scrooge's nephew. "But you
don't keep it."

"Let me leave it alone, then," said Scrooge. "Much
good may it do you! Much good it has ever done
you!"

"There are many things from which I might have
derived good, by which I have not profited, I dare
say," returned the nephew. "Christmas among the
rest. But I am sure I have always thought of Christmas
time, when it has come round--apart from the
veneration due to its sacred name and origin, if anything
belonging to it can be apart from that--as a
good time; a kind, forgiving, charitable, pleasant
time; the only time I know of, in the long calendar
of the year, when men and women seem by one consent
to open their shut-up hearts freely, and to think
of people below them as if they really were
fellow-passengers to the grave, and not another race
of creatures bound on other journeys. And therefore,
uncle, though it has never put a scrap of gold or
silver in my pocket, I believe that it has done me
good, and will do me good; and I say, God bless it!"

The clerk in the Tank involuntarily applauded.
Becoming immediately sensible of the impropriety,
he poked the fire, and extinguished the last frail spark
for ever.

"Let me hear another sound from you," said
Scrooge, "and you'll keep your Christmas by losing
your situation! You're quite a powerful speaker,
sir," he added, turning to his nephew. "I wonder you
don't go into Parliament."

"Don't be angry, uncle. Come! Dine with us to-morrow."

Scrooge said that he would see him--yes, indeed he
did. He went the whole length of the expression,
and said that he would see him in that extremity first.

"But why?" cried Scrooge's nephew. "Why?"

"Why did you get married?" said Scrooge.

"Because I fell in love."

"Because you fell in love!" growled Scrooge, as if
that were the only one thing in the world more ridiculous
than a merry Christmas. "Good afternoon!"

"Nay, uncle, but you never came to see me before
that happened. Why give it as a reason for not
coming now?"

"Good afternoon," said Scrooge.

"I want nothing from you; I ask nothing of you;
why cannot we be friends?"

"Good afternoon," said Scrooge.

"I am sorry, with all my heart, to find you so
resolute. We have never had any quarrel, to which I
have been a party. But I have made the trial in
homage to Christmas, and I'll keep my Christmas
humour to the last. So A Merry Christmas, uncle!"

"Good afternoon!" said Scrooge.

"And A Happy New Year!"

"Good afternoon!" said Scrooge.

His nephew left the room without an angry word,
notwithstanding. He stopped at the outer door to
bestow the greetings of the season on the clerk, who,
cold as he was, was warmer than Scrooge; for he returned
them cordially.

"There's another fellow," muttered Scrooge; who
overheard him: "my clerk, with fifteen shillings a
week, and a wife and family, talking about a merry
Christmas. I'll retire to Bedlam."

This lunatic, in letting Scrooge's nephew out, had
let two other people in. They were portly gentlemen,
pleasant to behold, and now stood, with their hats off,
in Scrooge's office. They had books and papers in
their hands, and bowed to him.

"Scrooge and Marley's, I believe," said one of the
gentlemen, referring to his list. "Have I the pleasure
of addressing Mr. Scrooge, or Mr. Marley?"

"Mr. Marley has been dead these seven years,"
Scrooge replied. "He died seven years ago, this very
night."

"We have no doubt his liberality is well represented
by his surviving partner," said the gentleman, presenting
his credentials.

It certainly was; for they had been two kindred
spirits. At the ominous word "liberality," Scrooge
frowned, and shook his head, and handed the credentials
back.

"At this festive season of the year, Mr. Scrooge,"
said the gentleman, taking up a pen, "it is more than
usually desirable that we should make some slight
provision for the Poor and destitute, who suffer
greatly at the present time. Many thousands are in
want of common necessaries; hundreds of thousands
are in want of common comforts, sir."

"Are there no prisons?" asked Scrooge.

"Plenty of prisons," said the gentleman, laying down
the pen again.

"And the Union workhouses?" demanded Scrooge.
"Are they still in operation?"

"They are. Still," returned the gentleman, "I wish
I could say they were not."

"The Treadmill and the Poor Law are in full vigour,
then?" said Scrooge.

"Both very busy, sir."

"Oh! I was afraid, from what you said at first,
that something had occurred to stop them in their
useful course," said Scrooge. "I'm very glad to
hear it."

"Under the impression that they scarcely furnish
Christian cheer of mind or body to the multitude,"
returned the gentleman, "a few of us are endeavouring
to raise a fund to buy the Poor some meat and drink,
and means of warmth. We choose this time, because
it is a time, of all others, when Want is keenly felt,
and Abundance rejoices. What shall I put you down
for?"

"Nothing!" Scrooge replied.

"You wish to be anonymous?"

"I wish to be left alone," said Scrooge. "Since you
ask me what I wish, gentlemen, that is my answer.
I don't make merry myself at Christmas and I can't
afford to make idle people merry. I help to support
the establishments I have mentioned--they cost
enough; and those who are badly off must go there."

"Many can't go there; and many would rather die."

"If they would rather die," said Scrooge, "they had
better do it, and decrease the surplus population.
Besides--excuse me--I don't know that."

"But you might know it," observed the gentleman.

"It's not my business," Scrooge returned. "It's
enough for a man to understand his own business, and
not to interfere with other people's. Mine occupies
me constantly. Good afternoon, gentlemen!"

Seeing clearly that it would be useless to pursue
their point, the gentlemen withdrew. Scrooge resumed
his labours with an improved opinion of himself,
and in a more facetious temper than was usual
with him.

Meanwhile the fog and darkness thickened so, that
people ran about with flaring links, proffering their
services to go before horses in carriages, and conduct
them on their way. The ancient tower of a church,
whose gruff old bell was always peeping slily down
at Scrooge out of a Gothic window in the wall, became
invisible, and struck the hours and quarters in the
clouds, with tremulous vibrations afterwards as if
its teeth were chattering in its frozen head up there.
The cold became intense. In the main street, at the
corner of the court, some labourers were repairing
the gas-pipes, and had lighted a great fire in a brazier,
round which a party of ragged men and boys were
gathered: warming their hands and winking their
eyes before the blaze in rapture. The water-plug
being left in solitude, its overflowings sullenly congealed,
and turned to misanthropic ice. The brightness
of the shops where holly sprigs and berries
crackled in the lamp heat of the windows, made pale
faces ruddy as they passed. Poulterers' and grocers'
trades became a splendid joke: a glorious pageant,
with which it was next to impossible to believe that
such dull principles as bargain and sale had anything
to do. The Lord Mayor, in the stronghold of the
mighty Mansion House, gave orders to his fifty cooks
and butlers to keep Christmas as a Lord Mayor's
household should; and even the little tailor, whom he
had fined five shillings on the previous Monday for
being drunk and bloodthirsty in the streets, stirred up
to-morrow's pudding in his garret, while his lean
wife and the baby sallied out to buy the beef.

Foggier yet, and colder. Piercing, searching, biting
cold. If the good Saint Dunstan had but nipped
the Evil Spirit's nose with a touch of such weather
as that, instead of using his familiar weapons, then
indeed he would have roared to lusty purpose. The
owner of one scant young nose, gnawed and mumbled
by the hungry cold as bones are gnawed by dogs,
stooped down at Scrooge's keyhole to regale him with
a Christmas carol: but at the first sound of

        "God bless you, merry gentleman!
         May nothing you dismay!"

Scrooge seized the ruler with such energy of action,
that the singer fled in terror, leaving the keyhole to
the fog and even more congenial frost.

At length the hour of shutting up the counting-house
arrived. With an ill-will Scrooge dismounted from his
stool, and tacitly admitted the fact to the expectant
clerk in the Tank, who instantly snuffed his candle out,
and put on his hat.

"You'll want all day to-morrow, I suppose?" said
Scrooge.

"If quite convenient, sir."

"It's not convenient," said Scrooge, "and it's not
fair. If I was to stop half-a-crown for it, you'd
think yourself ill-used, I'll be bound?"

The clerk smiled faintly.

"And yet," said Scrooge, "you don't think me ill-used,
when I pay a day's wages for no work."

The clerk observed that it was only once a year.

"A poor excuse for picking a man's pocket every
twenty-fifth of December!" said Scrooge, buttoning
his great-coat to the chin. "But I suppose you must
have the whole day. Be here all the earlier next
morning."

The clerk promised that he would; and Scrooge
walked out with a growl. The office was closed in a
twinkling, and the clerk, with the long ends of his
white comforter dangling below his waist (for he
boasted no great-coat), went down a slide on Cornhill,
at the end of a lane of boys, twenty times, in
honour of its being Christmas Eve, and then ran home
to Camden Town as hard as he could pelt, to play
at blindman's-buff.

Scrooge took his melancholy dinner in his usual
melancholy tavern; and having read all the newspapers, and
beguiled the rest of the evening with his
banker's-book, went home to bed. He lived in
chambers which had once belonged to his deceased
partner. They were a gloomy suite of rooms, in a
lowering pile of building up a yard, where it had so
little business to be, that one could scarcely help
fancying it must have run there when it was a young
house, playing at hide-and-seek with other houses,
and forgotten the way out again. It was old enough
now, and dreary enough, for nobody lived in it but
Scrooge, the other rooms being all let out as offices.
The yard was so dark that even Scrooge, who knew
its every stone, was fain to grope with his hands.
The fog and frost so hung about the black old gateway
of the house, that it seemed as if the Genius of
the Weather sat in mournful meditation on the
threshold."""

class base64_simpletest(unittest.TestCase):

	def testSmallString(self):
		shortString = "The quick brown fox jumps over the lazy dog"
		a = base64.b64encode(shortString)
		b = ft.base64(shortString)
		self.assertEquals(a, b)

	def testSmallStringDecoded(self):
			shortString = "The quick brown fox jumps over the lazy dog"
			b = ft.base64(shortString)
			self.assertEquals(shortString, base64.b64decode(b))

	def testSmallString_1(self):
		shortString = "The quick brown fox jumps over the lazy dog"
		a = base64.b64encode(shortString)
		b = ft.base64(shortString)
		self.assertEquals(a, b)

	def testSmallString_2(self):
		shortString = "The quick brown fox jumps over the lazy dog!"
		a = base64.b64encode(shortString)
		b = ft.base64(shortString)
		self.assertEquals(a, b)

	def testSmallString_3(self):
		shortString = "The quick brown fox jumps over the lazy dog!!"
		a = base64.b64encode(shortString)
		b = ft.base64(shortString)
		self.assertEquals(a, b)

class base64_binary(unittest.TestCase):

	"""http://octodex.github.com/images/pythocat.png"""
	pythocat = "iVBORw0KGgoAAAANSUhEUgAAA4AAAAOACAYAAABrNB1XAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA2ZpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDpGNzdGMTE3NDA3MjA2ODExOERCQkFGRjk4MjU2RTdGNyIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo2NUFENTU5Qjk2MjkxMUUxQkYwNUIwNTU1MkIzOUQ3RiIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo2NUFENTU5QTk2MjkxMUUxQkYwNUIwNTU1MkIzOUQ3RiIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ1M1IE1hY2ludG9zaCI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkIzMDBCNjE4MEIyMDY4MTE4REJCQUZGOTgyNTZFN0Y3IiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkY3N0YxMTc0MDcyMDY4MTE4REJCQUZGOTgyNTZFN0Y3Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+msNJVgAA2thJREFUeNrs3X+MlEee5/kAFxgw4ATaNm63Ox9q8fR1z06TeHZ65O67JulbafewZil6T+dV3x9kbWu00s1JFLf3x0nrE4Xkk/aPvS2QbqUbnXaq0GlbamlvKGZkdm51mkpmp8fTPbuuxN61p2226knTGAwGCgpDQRVwzzczHldSlb8zn3ginuf9kh4nLorKrHiezIxPxjci1jx+/FgBAAAAAJJvIK2/+Jo1azj7AIDEGcxmc8FNps5f5Rv8k2eDI9fix3r6sN1ccJRafI8fHOUGf1es9/0z5bLPlQUkS5oHwdak9ZcnAAIALAtumRVBbGXoqhfUGoU9RMvXR61zTcLkXBAiSzQbQAAkABIAAQDJDHP5BiEtuyLU5WmtVJIwOFcTHCuBMgiJRZoGIAASAAmAAID4A51XE9xqA90+whwiCIdFHQyLQSico0kAAiABkAAIAOhvsKstv9xTE/AIdYjbZHCckVvCIEAAJAASAAEAjcNdOFIXhrzaOXQEOzgbBoMgOEFTAARAAiABEADSFO7CEbvakbt9hDukhB8cp4LjBKOCAAGQAEgABICkhLx8TcB7tk7gA6DURHAcZ6sKgABIACQAAoDtAc9T1dLMMNiFc+/ytA5AEAQIgARAAiAAuB/y9ilG8YCoSDnoSUVpKEAAJAASAAEgwpAXBrow7O2pCX0AzPOD42gQAidpCoAASAAkAAJAt0EvDHh5tTwnr3ZPPAB2KQbHMGWhAAGQAEgABIBmQS8czZPbbE3oA+AeKQWVuYEnaAqAAEgABIB0Bz2vJtxl1fKIHoDkkXLQYeYGAgRAAiAAJD/oZWrC3R7FiB6QVhL+DgUhsEhTgABIACQAAkAywl5t+eY+tbwwCwCEjlISCgIgAZAACADuhb28YlQPQHcmghA4TDOAAEgAJAACgH1BLyzhzCu2WADQP6Xg2M+8QBAACYAEQACwJ+yFJZ0AEFUIPMRWESAAEgAJgABA2AOQDjICKCOBJZoCBEACIAEQAPoX+PJqec5enrAHgBAIEAAJgARAAMkIe7kVYY85ewAIgQABkABIAASQgLBXW8q5T/85Q8sAIAQCBEACIAEQgPuBLxzdC8Meo3sAkoTVQUEAJAASAAGkOvDlFaN7QDeKPfxbnmuEQIAAGIEBTj8APBH2MjVhL68Y3YN7fH2sdK7D7w/NuVQOGDyHPdV8gaVMk+f1vjpfa/XzkkraaCw42CweSBhGAAGkPfB5KwKfR6sgRhK05pqEtuLK8Mb+bbG8bqwcnVwZErMr/t/l0czjwTU2yllH0lACSgAEkK6OWxj42HcPUZnTYa5ekKsNeQS49IZHeR2SVYKHHHjYUgpa5OyBAEgAJAACcC3w5RVzitA9Xy2XSkqIu6X//GXHmE4yunydkhB4MDgKlj5E+cBiF/MBQQAkABIAARD4kLRgd27l1wh1MPj6Ja9XI8FxxMLXrmLwXNjPWQIBkABIAARA4IML4U5GLs6HHVl9W2JEAwTBjhwNnjMnOEMgABIACYAATHaMvJrAN0TgS71wPl1Ykhn+P3PrkKQgeMyShyTPrb08t0AAJAASAAFE3QGSwHdQsUpnGvn6WBnwGL1Dml4HpdJhXNmxLQ2loCAAEgAJgAD63tmpDXzsw5d8Yag7p5ZH8xjBA1a/No4qO0YDDwXPz0nOCAiABEACIIBuOzXhPL4w9IGQB6Dx6+VpFW81hDx3d3E2QAAkABIAAbTbgZGyTpm/xzy+ZAmDXViuWSTkAZG9hkoIzMf4MNggHgRAAiABEEDTDot0VCjrTAZfH+fCP7NVAhDL66rMCyzEdPfsDQgCoKMGOP0AIuqYeOrJsk5G+dxT0gHvvFou2SzRLIAdgufjcPBaKwFsJIa7D1coHeVMAG5hBBBAP0NfbeBjlM8dvmJED3D5tbegqquEmsYoIJzFCCAAdNfpCOfyMcrnDgl2MopXVtWtFAh6gOOC5/GErrowvUKovOZL+GRzeMAhjAAC6DT05WpCH6N89vJ10AvLN0ssxgIk/vU5jjmBrAgKJ7EIDAEQQPNORe0on0eLWKdUJ+xRkgWk8/VaVgcdMny37AsIAqBDKAEFUK8D4anlBVyGaBF7wx4lnABWGFbV6gzP4H0eDg4CIOAIRgABhKEv3Iz9sKK0k7AHwPXX82nDd7uNygO4hBJQAiCQ1k6CBL5wlM+jRQh7ABLz+i5bNIwZvMthWYyGlgcBkABIAATs6xQM1YQ+Vu2Mh18T9oqKOXsAonm9n1LVyg4TJoPXsUO0OgiA9mMOIJD8DkDtVg3M54tHUQe+c4rVOAGYc1SZKwXl/QVwBCOAAKEP/eXrwFcZ3QvCXokmARDj+4HJrSFYDRTOYAQQQBLe5D0d9ljExSwJe+HoXpFSTgCWOW4wAO5TrAYKEAABEPoSZE49ObpXpEkA2ExKzoP3iglDIZD3IcABlIAChD405ivKOQEk431j1lDgpIMFJ7AKKAEQIPShNvCF5Zw+TQIgIe8jplYE3cuHZSAA2o0SUIDQl2alFYGP+XsAkuqUoQDo6ddWAARAAG2EPlm9s0DoI/ABQJ8VDd2PvHexEAxAAATQIvSxZQOBDwAioxeDKanoP1zM0toAARAAoc8UXzGHDwAaKRoIgB7NDBAAASwHv9rQl6FFehZuy3CGwAcALZVpAgAEQCD60Cefth4h9PVNbeBjoQEAaJ+J10zmrwMEQCCVoc+rCX0eLdJzh6US+th4HQB6YmIeNB90ApZjH0Cgf6GPFTz710GRFeRkHt8kC7cAQF/fqyLv+LEZPFzAPoAAenkzldDHYi69KSrKOgEAAAiAgKWhj3l9vfFXhD5G+QAAAAiAgFWhz9OBT4KfR4t0rDbwMcoHAObfx/K0AgACIND8zTLcr0/m9fHG2ZlwLh+jfACQHj5NABAAAReDHyWe3SnpwDfJKB8AEAABEAABm0Ofpyjx7EbtKB9v/AAAAARAwOrgF5Z4sopne74s7QwC3yTNAQAAQAAEbA99UtY5ooOfR4u05OvQd4rSTgAAAAIg4Erwk7B3TDG3rx0S9E6p6nw+n+YAAOflaQIABECkLfgVaI2mwvl8k6zaCQDogk8TAARAIM7gF5Z6HqM16pKQVyT0AQD6pEwTAARAIK7wFwY/Sj1Xhz4WcQEAACAAAokIfrKH33hw5GgNQh8AAAAIgEhu+BtVlHsS+gAA9TxLEwAgACIpwY9RP0IfAKA5KmMAEACRiPBXCG7GVHrn+hH6AAC2YK9YgAAIRBr+ZNSvQOgDAMCa9ycABECg78FPRvumVLrKWQh9AAAAIAAideEvbfP9JOydIvQBAACAAIg0hj8Z+Uv6fL/KSJ9ic3YAQP+wLy4AAiAIfxaRifOngmOC0AcAiACrgAIgAILwFzO/JvT5nGkAgONYBRQgAAKEvxXCxVxOBqGPN0oAQGJQwQIQAIFew18mQeGPxVwAAABAAAQSHP5khO+kYjEXAAAAEACBplzd6sFXyyWePqcRABA3/aEqABAAYe0b1WhwM+TQQw7n9UmJZ5EzCACwDCuAAiAAwtrwlw9ujjnycCXsySqelHgCANKOhc0AAiDQcfiTEpVxyx+mryjxBABgJT4IBQiAQMdk5M+z9LGxiicAAAAIgEA/6NLPEcselnyaKat4slE7AAAACIBAH9lU+ilh73gQ+iY4LQCABPBoAgAEQFhDr/ppw5tTZcQvCH6jnBUAAAEQAAEQ6H/4k4VfjljwUCaC4yireQIA0JVzNAFAAATaIfP+4tygVgLfIfbvAwAAAAEQiJAFo3+youcwo34A6pDXp1ydP7fi60MUaUYAAAEQWBbn6N9x5voBqZevCXdZVZ0nFR79Ih8wlfRxXodCn6YHABAAkSoxj/4Ns8InkCqeDnly7NG3nqH7zuigma/5mgTAyt6iOhgCUcvSBAAIgIjbkIpn9I/wByRfGLj2qOVRPtsC6Yg+fB0EJxQjg4j2mgMAAiBiFcfoH+EPSHbg26eeHGlzpWN+TB/y+nScIAhHFWkCgAAI1DWYzYalWIQ/AN2GJgl6B5WdI3zdKuhDQuAJVZ0/CAAAARDOO2z4/iYIf4DzcjrsHVbmP0Ay7Zj+PYcVoyoAAAIgEmDI4H3JAgtHaXLA2dB3WL9meCn73eX3nVLV0cBRLgUAAAEQTtLlnyY7cuzzB7gXfAo6+Hk0R2U0UBazkdFAXsvQy/MKAAiAiIXJ0T/Z648l1gH7ZWpCX47mqPu6KR34/YRAEAABEADhmn2G7kc6SSdobsBqEvoOKrMfDLlKgvEUIRC2mimXi7QCQAAE6skbup+TlH4C1gaZIyq+vUAJgQCA1FpLE8CkwWzWVPhj9A+wiwQ92fR8Wh8Fwl9PIXCMZgAAdIMRQMTRcTFhgtE/wAp5VZ3XV6Ap+kra87zigy4AQIcYAYRpewzdz0maGohNuKDLrKqWKxL+oiGjgCyYg5b06tsAQABELDwD91GaKZd9mhqI5fk9roPfuGLVQRPGaQK0wUS5NVU3AAEQqCtv4D6KNDNglCzmMqWDX0Ext88kGdkZoRlgAbZcAgiAwJMGs1lTncIztDYQuXBRFwl9p5W51X2x2jFCNwCAAAgbmZqDwKeQQHQ8tVzmOaYo87QljB+jGQAABECkkc/qn0BkcooyT1uNEMYBAARA2MZE58SnmQGeXyl1hCZAA6wCCoAAiMQGQMo/gejI6PokzWCtgmJkFvWxCigAAiAS6xZNAESKRZbs7uQXaAbE5DxNABAAAQDJwwig3SgDBQAQAAEAfUMZqN08xXwvAAABEADQR5SB2u0wTQAAIAACAPqFEUC7DdEEWGEPTQCAAAje5AB0S8pAWXHXXp6iDBRPYhVQAARAxMJPyJscAKVO0QRWowwUpvGhEEAABGIJgHzqDZhBGajd8jQBAIAAiDTIDGazjAIC0fMVn/jbTD4M82gGAAABEHEy1VlkFBAwgzJQu+VpAgAAARCxmSmXTU0Qp9MDmEEZqN320QTgfREAARBxK9LpARLDV2bm9qI7VEPA9OsBAAcM0AQwzMQoYF7mARoccQTSTEYBRxx/TSrp2/NNvk8+WPKUW/PqJABmFMvzw4DgPZcACBAAgbqkg2Vik2K5jwmaG4jcKYcCoHRQi/p1qFQT/DohATCvqtss5B0JgUUuUwBAiBJQmGaqI3KQpgaMKCl7S7/ksZ0IjkPBsS04dgXHsP5aUXU3Mia/60Rw7Nc/z/Z5kJSBAgAIgIi9Q2bCENtBAMbYEoJWBr69wXFUP74oyiB9fV+HlL1llnu4PAEABEDERs/LMxYCaXHAiLi2g5AANmEw8DULwPuVnSOhHpdnug1ms3laAQABEHErGrqfwzQ1UFkEZEpF+4GIyTLQSR3yJOyFJZ2mA1+jNrBxJJASUJjg0wQAARBo5pyh+5HVQD2aGymW0+EvbyAIFCPsWE7ocLVG355Q5ioJugmBtn0AABAAARAAEauiwfuiDBRpldfhLwx+Ue+PeabPQeq4Wj3K58rr2wQhEABAAAQ0PQ/QVAikDBRpVNDhr7bjH/UIYK9lmGFp5y4d/EaVnaN87Thq2eOhDBQAQABE7M4Yup8cZaBImXF9rJQxFAI7/X4Z3ZMFXMLSTj8B50CC8ASXIizBCDAAAiCsYLKc6wjNjZR08mTUr9Dke6IOgGfafO7Xhr4JZe8WCr04ySUJSzACDIAAiPjNlMu+MlcGyjxApKGDN62q8/6aiXpPuEZloGkJfbVMrowKxI1rHSAAAm0xtXeYN5jN8gkokko+4JCRP6+N780beDzFFIe+Rm0BJF2ZJgAIgEA7TJaBshgMkmgkOE6r9uf4mPgg5GjKQ1+t81yiAAACIKDp1UBNhcACLY6EkYVexrr4d/mIH5ef8tBXy5ZVTIucCgAAARC2MLUaaGYwm2UuIJJARvtkvl+hy39POTSQLs/SBAAIgLDGTLk8ocyNFhykxeG4cLGXXkLcPpoxVUo0Aa8bNAEAAiBsY6oMlBFAuKyTxV7oDNohb8Fj8DkNMIAPGgACINARk2WgBZobDup0sZdmPMXG0KZkLXgMLEQDE5j3CxAAgfbNlMuTijJQoJFuF3tpJk+zGmFDOxc5DQAAAiBsNGHofoYGs1lGP+CCXhd7aYYy0OhJG3sEQAAAARCo75TB+2IuIFwID7MRBjUWgomeDXuPTnIaoCj5BkAAhI1mymWZQO6nqGMGNFJQ1cVeouy0MQIYfYe7YMHjOMOpAM93AARA2MzUp9X5wWzWo7lhoVFVnfMX9Sf2GTqFkYf4uEdd5hQjgDCHVUABAiDQlZMG74syUNgko4PfMYP3SQCM7lwes+BxmFxcCyk3Uy5zrQEEQKCrNxBfmfsUkTJQ2BQYpOSzYPh+99D0kTim7JhzdZxTAQAgAMIFphaDyVEGCgtEvdhLM3maP5I2HbHgcUwoNoAHABAA4QiTc1aO0NyIUUFFv9hLq/CJ/gnLeG3A6B8q+KATAAEQ1tNloEVDd8c8QMRlVJlZ7KWVPKeibyTM29DZlvDnczqgEQABEADhBFNloN5gNssoCEySwHda2bFIiOD6749xS9pSgt8JTgcMYwVQgAAI9MxkGSiLwcAUT1VHiWwaeWZD+P4E+oIlj2dYsfInzOOaAwiAQG/0ctKmQmCBFocBMjo0rewbcWMEMDmBXkb+ipwWAAABEK4yVQaaGcxmmQuIKBV0+MtY+Ng8Sx+X7UYsC/RSgneU0wIAIADCWTPlsslNjA/S4ojImLJnZchG8pymjtpqSp9XW4KzvE4e4tSgAY8mAEAAhEtMlYEyAoh+C+eGjTjwWCkDbd2BlvM4q8OfbYF5v2LVTxAAARAAkRBnTHXWB7PZAs2NPna4bFvspRkWgnkyuEvAG9UB/qYOfmOWdqRl0RdWYETcztEEgFsGaALYSspAg2DmG+p4SRnoBK2OHuVUvJu7d/uY0yqvf/89+talthjmNQsAQABEEkkZqIkyuqEgbGb0CqRANwrK/vl+9WR08En6SJKnA18Y9vIO/y4nCH8AAAIgkuqUMjePaohOFbo0ptyY71fPRALDX6Ym5O3Tf07Saqcj+vVqUr9GUgYKACAAIhlmyuWSwTLQwwRAdBE0Tit3R5OSUkaYV8ulnHmVjoUvPB0E5fAJg2ggSxMAWIlFYOACU3sC5oOw6dHcaFM438/F8CelzvsdDX/yHC2o6qirtP9jtbw1Q0Glc9XDMAxO66PA0xM11wYAEADhHJOdVLaEQFsfFujQ4eICKjJCtDc4ig619ahu73BVznEdePJciqvkdPvMKnfLkuGWIk0AEACBvpopl31lrqzpMC2OFgrKvZU+QxPKvX3j5Dl5TIe9DJdf2zxVHRWdVYwIAgAIgHCQqTLQHGWgaGJcubnSpziuqnP+XFvplj3Geg+Ccs26OmINACAAIqUmDd7XEZobK2R0B7rg4GOXwHdIVcsoXcSiJv2R19cwZaEAQAAE7KfLQE2FQOYBopbLi71IeNqvzH6AQgC0l3yQIWWh4zRFql6/AIAACGedMXQ/3mA2y5smlHJ7sZeiDn9JCFBFLsW+KqjqaqHMqUxH6I/aHM0MEACBqJgcxWAxGIwodxd7OaHDX1I6ZswD7L+cw9c3LCL79dIKAAEQiOpNZs5gCCzQ4qkmJXJjDj5ueY7IQi9HE3Y+6GBGGwIBAARAwFqmVgPNDGazzAVMHxkNcXUjbZc3dycAxhsCmRMIAARAwE4z5fKkMlfWdpAWT11HeFq5u7n7rgQHJV+5tXehawqKqgcAIAACFjO2GuhgNsv8mHSQ0V4phfMcfOwTwbFXJX8hBkYBozXm6PWPBljMDAABEEliajXQjGJLiDSQxV5OKzcXwxjWRxqc51KN/PWOUtDkndOosQIoQAAEoqfLQH1Dd0cZaLK5vNhLUuf7NVLkco1cXvGhFzrDyDxAAASMoQwUvXB5sRfpcO1NYSAiAJoxRhMAAAEQsNEpg/fFJ+LJ4vJiLxOqOvLnp/TcMdoQPU+xIAwAEAAB2+iNZ011go/Q4onh8mIvx1V1vl+a59wQAM04RhMAAAEQsJGpUcDcYDbr0dzOG1VuLvYige+Qfvxpd44mMEJe7/I0g/NYBRQAARCJM2HwvigDdVe4uqGLoxoy4iUln5Ocxi/bA2ZQ+ZCM176osQooQAAEzJkpl32DHcLDtLizHSAp+Sw4+NiLOvwRegiAcRhSbm6NArPYngUgAALGmSwDpZzGLXK+ZpWbZVAndPjj0/X6wRhmFGgCACAAAraZMHhfjAK61XGVkT8X5/vJQi9HOYUNMQ+Q1zwAAAEQaTVTLkuH2diegLS4E0ZVdc6fi+EvbZu7d4MyUHNyijJQAEicAZoACXDGUDjzpAxUb0EB+0hHVTaxLjgaaij5dD8AFhMYpuS1dYLLzkn7aAIABEAklYwAjhu6L1kZb5gmtzL8TSl3N3fnmmqfrw8v5hAqYe+8fizFDq5TuUYP6mDlOdDe+wiAaPF8BOAYSkDhPF0GaqqDQhmonUYcDX/DhL+uA5jJDq68vsi8TBmlXRMce/X/T6jOFqWZ098v/3aX/nlFy9s6z+UGAiBAAARsdMbQ/WQGs1lCYLoDQT8w36835yM8LxLIjuvzs00HNQnpJyIIa0V9P4eUveW/nnJjpBIAQABEmsyUy5MGO1AHaXECYI+Pda9iO4Neg1O/fs4JHfB26cAngWxU/52p15RJff+2Xsd5LjkAIAACNjK1GmhhMJtlZTy7+MqNBVQmdMDwOWXGA6CvVpdy7lfLpZxxn5NwVNjGELiHSw4ACICAjU4ZvC/KQJMRCkySssJhxUqf/VJqEaaKylwpZ79DoG3XSI7LzUl5mgAAARCJNlMuS6fON3R3lIHa57ylj0s68zLHa5RTFFkALOpgd0jFW8rZz+uFIAEX+DQB4J41jx8/TucvvmYNZz+BBrNZ2QduxNDdbdMrkMKeTuqUhSFlWLF5eRQ8Vd1WIaltO2VZ8NrLdezc+2HkHbzgPZDOFJyV1gwkGAFE0pgsAy3Q3NaFLZsUlb1zupLAT3jbHrfs8VAGCgAEQMA+M+VySZkrSTlMi1tlzqJAcELZOZcL7ihaFnA9TgkAEAABW500dD+5wWyWTpFdSpY8hjOcCvTBKYseCyuBAgABELDWpMH7YjVQu9iwEIyUysn8rZvBcVpVS4X5oADdKFr0WNj6xiGD2WyeVgBAAERqzJTLvjI3EnSEFqfD3KTDLB8QjAfHbHBMB8cYHxqgA/I6ZksZMYECK/k0AUAABGxiqnTKG8xmWRzBrg6zreQ6kRVqZVTwsb6V//c4bXD0mgYBEAABELDGhMH7YjEYuxQdeZwyEigjgrP6GNdfo9QOtnay+bALAAiAgJ30/nym5gJS0mcXF0dMPFWdKyijgjJ3UOYQjtLhRqBs0WPhwwkAIAACVjO1EqPHhHurnEvA7yDX0zFVnTcogXBcB0Q64AAI6wAIgEADMgJoagEFykDtkbQ5Uxkd/sZ1GAwXk8lzqmGYRxM4g+oBAARApA9loKnlq2QvThAuJlO71QSLySTXswRAWIoFigACIGAlU2WgmcFslhBIx8S0cKuJ2sVk2GoieYEfsNEtmgAgAALWmSmXKQNNp/Mp/b099eRWE1P6/wkRBEAAAAiASA1jZaCD2SwT7+1QpAkq8qo6IijzBtlqwj2cKwAAARDowknDHTYQAG3kqSe3mpBQOKoYYbLZQZoAXXqWJgBAAERqzZTLMh/Mp8OWOixQ0JwEv9qtJk7rgOjRNFYFdqDb5zcAEACRaibLQOlAEwBdEy4mIyWis4qtJmwwznMKvMYCIAAC3Ttl8L4oA7XDOZqga7VbTchiMmw1YdaIpeF7jlMDrgeAAAg4QZeBmvq0ktVA7cCn0/1Tu9XEKM0RqYJuawAACIBAj0yNAuYoAyUAJtg+miDS8DfOcwoAQAAE+mPS4H0dobmtUKQJ+i5PE0Ri1PLwJyj5cwfbhwAgAAIz5bJvMBAwD9AOzAOMBisM9rctZa7lMcsfZ5FTxXMUAAEQcJGpMlBvMJvlDTh+lKzRubSVjNDIXD9ZcTXvwOP1OWXg9RUgAAIuMlkGymIwdFCSinmA3fPU8nYbIw497vOcOtSaKZcpCQYIgIAzb1imQmCBFo+drxi5iAIjgJ3J6NeDKR38Csq9OVpFTiMAEAABV50x1ekbzGaZCxg/RgEJgHHwVHWET/ZQvKmqo355R3+XOZ5HAEAABJw1Uy5PKHOr2R2kxWN3VB9FmqKv8jTBqvYIA9+sPmSOXxI+BJrk9LqDbYgAtDJAEyClpENTMHA/0vkbprlj5QfHCX2E52SfvqWj1FvgSWOoltLNnP79s/rPSR8RPcPl7hRe1wAQAIEGHRoTAVDKQAt61BH2hH85juqOknTkD+pb9s5q356UBL3ciqCXtmvE5LxpuKNIEwAEQMApQSCbDILZnKHOnIQLAqCdfH1uwvMjHfwhfc6Y59ZcEtonDHmePvbor+U5vV8i/AEAARBIDOn0m1iGfSgImxmWzHZCSR+jNUEgHB30aJ4nhKHJt/xx5lfc7lvx/2juJE0AAARAIClOKXP7cA0pRgFdE5a+TdYEntr5g6iOnvkx33+mJow+q5ZHJgl4vSsqVv8EAAIgkBQz5XJpMJv1lZmRnSMEQOfJtVK7mIwEjHB0MK3lojkVXYmgp54ceQ3LMzOK8lxTjtMETvJoAgAEQKAxGQU8ZqKjLEtzB6HTp8kTo6iWF0KQUFI7OpiWhUL2RfizpR3HuMysuL5BAASQIOwDiLSbMHhflA0m15y+lmTLj23BsVelY+/BfIQ/m9LDeB2lCdDEOZoAIAACTtIjcqY6modp8dSQa0pKRfcHx5rgOKT/30/g70o5ZvKcIIADAAEQSLJTpjrKg9ksneV0Cvcd3KWPYf21JKwMG9U1TQCJh6+Y+wcABEAgBZ1zUxgFhHSwJ1R1VDAsFz3ucOCJah4g26bE4xBtDwAEQCDRdBmoqRDIPECsFO47uFcHwkM6IPqOPP4oR7V9Lg+jhhUjr0mQpQkAEACB1s4Yuh9vMJvN09xoINx7UDriYbnoUWV2lJoAmE4Tiq1qksKjCQAQAIHWKAOFjSQAyYIcMiooi8nsV3Yu0JGPMBDDTPgbphnQgSJNABAAAafNlMvhMv4mUAaKXjpdMiIo5aLhYjITFgSlqALgeU454Q8AQAAEomKqDDQzmM0SAtErX9mz9+AeTgfhDwBAAAScMlMum1yW/yAtjj6r3XswXEzG1N6DbAVB+AMAEAABJ5maC1gYzGYzNDciEi4mY2rvQU9Fs/AEcwCjMUz4SzT2mwVAAAQ6cMrgfVEGClN89eTegzJK2O+9B3MRPW70tz33Klb7TDoTHy7y4QxAAASSYaZcLhrsdFIGirjIdT6q+rv3IAHQbpP6fFNWi368V3IdAQRAIHEdJROGBrNZj+ZGzFbuPRguJtPp82BfhI8PvYXoQ/qgLQEABECgDspAkWbhYjKd7j2Yj/DxoDvHdaCfpCkAAARAoAFd2mKq08mm8LBdUbW/9yCLT9hhQp+rUcWoHwCAAAi0xdQoYI4yUDjEV833HowiADIC2HnwG1bMn0yl4P2ED2EAEACBLpksmTpCc8NRK/ceLEZwH7do5qbm9Dkg+EGwAigAAiDQjZly2VfmRh6YB4ikBJEowgeBpnH4DhfuOUo7wfC1B4AACCTSSUP341G2AxAA22wLGe3bq5b382M0BgBAAAT6xGQZKIvBAPWlPeDUhr5wtI8RGAAAARDot5lyec5gCCzQ4kBdaQw7RfXkyquEPgAAARAw5Iyh+8kMZrPMBQTSSQKf7Nkni+l0svcisFKeJgBAAAR6MFMuTyhzJWgHaXGgrlLCfhd5XQlH+MLAN6qiWUUV6DfmnQKOG6AJgJakDLRg4H6GBrPZo7r0FIDbHU5fH+f0bUkxoodkOE8TAARAIOnOGAqAsn+TlIFO0OTAqjBlazAt6cdX1n+WrxU5ZQAAAiDgqJlyeXIwm5UOnmfg7g4SAIFVyjHdb7EmgJZrAl94CwAAARBIKCkDHTFwP1IGmqEMFIiEr5ZHE+U5dr7mz6U63wMAAAEQSKlThgKgKKjqCoAAquQDmH01/18b3mqFo3OqTrAD0mAfTQCAAAj0wUy5XDJYBnqYAAisCnb7aQbACj5NALiNbSCA9p0ydD+5IGx6NDcAgAAIgAAIxGfC4H2xKTwAAAAIgEBcZsplX5mbT3SEFgcAAAABEIiXqTJQbzCbzdHcAAAAIAAC8ZkweF+HaW4AQAfyNAEAAiDQR3p/vklDd8c8QACAbXyaACAAAmlzxtD9SBkoIRAAYA09Hx4AARBIFRkBnDN0XwdpbgAAABAAgZhQBgoAAAACIJAupspAM4PZbIHmBgA0E7xXZGgFAARAICIz5TJloAAAm7B1EAACIBAxY2WgfLILALCATxMABEAgzU4avC/mAgIACIAACIBAXGbK5ZLBN8MjtDgAAAAIgEC8TJWB5gazWY/mBgAAAAEQiA9loAAAGzBXHAABEIjaTLnsBzclQ3dHGSgAoBFWAQVAAAQMOWXofrzBbJY3eABAXEo0AUAABGBuHqA4THMDAGJyiyYACIBA6ukyUGN7AtLiAAAAIAAC8Tpj6H6kDDRPcwMAAIAACMSHMlAAQJz20AQACICAITPl8lxwM2Ho7igDBQCsZGIbiDmaGSAAAlhmqgw0M5jNEgIBALU8A/fBKqAAARBAaKZcljJQU5+OUgYKAKgYzGYzhgIgAAIggBWMrQaq3/ABADC1R6xPUwMEQABPOmnwvigDBQCIvIk70dseASAAAqh5c5T5EabeICkDBQCIgwbug/AHEAABNGCqDDQ/mM16NDcApJd+HzBRAkoABAiAABqgDBQAkLT3gXM0NUAABFCHniNhaqlsykABIN2OGLoftoAACIAAmjhl6H5yg9lsjuYGgPQJXv/zytz2DwRAgAAIoIlJg/fFKCAApNMxQ/fjswIoQAAE0IR+oywaujvmAQJAyujRv7yhuyvS4gABEEBrpspAvaAjQAgEgHQZM3hfZ2hugAAIoDWTZaAHaW4ASIfBbHZEmdn6IVSk1QECIIAWZsrlOYMhkBFAAEhH+POUubl/YlK/nwEgAAJog6ky0EzQKSjQ3ACQeKflNd/g/VH+CRAAAbRrplyWEUBTn5xSBgoACTaYzcq8P5OlnyYrWQAQAIHEMFYGGnQOMjQ3ACQy/BWCmxHT71+UfwIEQACdO2nwvpgLCADJDH/jMdz1KVofIAAC6NBMuVwKbnxDd3eEFgeARIW/fEzhrxS8fxU5AwABEEB3TJWB5vQKcQAA98NfIbiZiunuT3IGAAIgADfeSCkDBYBkhL/xmO7enymXJzgLAAEQQJeCN1I/uCkZujvKQAHA3eAn2/qMxxj+xHHOBEAABNA7U5PpvaDzkKO5AcC58Cev3VLyWYjxYTD6BxAAAfSJyb2UDtPcAOBM8JNRv9Hgj9PK7D5/9QxzRgACIIA+0GWgpkJggRYHACfCX0EHv2MWPJwiK38CBEAA/XXG0P3Ip8ksBgMAFge/4JhV1bl+ngUPSTZ8Z/QPSIEBmgAwalKZm9h/UJktOwUANA99EvQKqlqm71n28E7qShUACbfm8ePH6fzF16zh7COuDsC4MlOiKZ/m7gre0OdodQCI7TU/H9zIIR/K2bpAl2z6vpezhTRJawYSjAAC5p0xFAAzqron4ARNDiDikOOp9ka0MhaHoLaCkqp+uNZITv+OWf1nF35XSj+BlGEEEIins3RTdxKiNjlTLh+ixYHUv+bk63y53teyDYKc68ENjQ2z7QPSKM0jgARAIJ7OmKkyULGLeR2A868Z4chSvTC2MrR5yr75ZbDTRPD+wOgfCIApQwkoEI+TBgOglIGeoMkBa0NdbWDbUxP0akMf0G9SznqUZgDShxFAIL7O36wy8yk9k/uB+AKep4PcszWBjlJKxI1FwpB6jAACiMMpZWbj35ws0EAZKBB54JPR9n064OVpEVgc/vYT/oD0IgAC8ZkwFADFEUWpDxBV6JPl/eWWck24QMJfiWYA0osSUCDezuO0MlMO5gdv+LtocaAvz1sJegVV/WDFo0XgEFb8BLQ0l4Cu5fQDsTpl6H68BsvAA+gg+AXHaPBHmb87RvgD4Q8AARBAp0y+GR+muYGuw19BBz8p26bUEy6RuX6HCH8AQpSAAvF3LE+r6vyhyDsBQQdgGy0OdPT8lBJtGe3L0xpwNPwx5w+ogxJQAHE6Y+h+MnoUA0B74W8kuJkm/MFRJcIfgHoYAQTs6GjeVGbKyiaDzsAhWhxo+nyU5+Jpgh8cVlTVsk+2egAaYAQQQNwmDd3PkO7cAqgf/qTkk1E/uOx4EPzY5w8AARCw3CmD91WguYG64U/m4k4pVveEm3xVLfkcpSkAEAABywVv2EX95m0Cq4ECq8NfQVXLPhkhh4ukimSvfi8BAAIg4NAbuAm5oLPr0dzAE+FvnJaAg3xVnevHfD8ABEDAQSbLQI/Q3ADhD047rqqjfpM0BYBOsAooYFdnVBafyBm4Kz/oNOyixUH4I/zBOROqutCLT1MA3WMVUAC2MDUK6OkFL4C0hr884Q8OBr9dQfAbJvwBIAACyWGylOcgzY2Uhj8ZZT9NS4DgByCNKAEF7OucSsfUxOjcnO5UsHAA15ynGm99MBdcI6UE/a6yyue0YqsH2E2C3kkJf7xGA9FIcwnoAKcfsM4ZQwEwo+9ngiZPVdDLB8ceVZ1rmlNtbHsQ/Lvwj0X9wcF5/eeSg53T04Q/WBz6pArkVJI+dAFgH0YAAfs66dIhn1Vm9iMrBh2N/bR6oq8lCfn7dPCLIvhIR1U+tJi0vdMatMdYcDPClQGLOPP8AZImzSOABEDAzo6qLE5RMHR3u5hXkqhrR4LeQR34cobvXq4jK0cwdLtMcYUgRr4OfC6PoAMEQAIgARBIQGf1RNAJOUqrO3uteGp5lM+mlV2lo3syuLYmLGgjk6PqaTSnz3c7AajchxDl9/gz8j3++30t/v5czZ8l6KngeVDkMgEIgARAAiDQqtMqHVbPUOeNxWDcuS4yugMbjvJ5lj9kua5O6g8a5mJqM1MLK9mspM9Fo6DS7PsqwYtKAQAEQAIgARCIttNqcr6SbCo8Sqtbey3kVoQ+F8USBPV+l0nZ8qFYG8jUk6NptX/HiBMAEAAJgARAONjp91S1bM1U55xRQHvOvWujfJ1ea/KBwwlD7Wh76Wc44haurlr7NYIcABAACYAEQKQsCMh+ZaYW8mAUMN5znYRRvk74wTEcZcCxrPQzXO0xDHcsAAIABEACIAEQWNWBLQQ344bujlFA8+e3dvEWL6XNMBEcR/t93Vm06qf8fseZPwcABEACIAEQaKcTK6VrN012VoOO6jAtH9n5lJAnweSgYlGSWhL+ZDRwso9tbWoRpUaK+nci+AEAAZAASAAEOurImtwTUOxn3lFfz19Ohz0JfTlapKlJHZrmemzz0eDmWIy/x1ETcxwBAARAAiABEMkMEKZXMfSDYy+loD2fsyQu4GKCXHeHuv0QIuaFX/o+kgkAIAASAAmASGegMF3OxubwnZ0fT1Ha2W9dLUpkePuUleFPRs9LnDoAIAASAAmAQK8BQzrCpkvaDjGS0fSchKt2HlaUdkalqK/DuTbPiQTx2RgeJ+EPAAiABEACINDXsBFHWZt0aveyiMUT50ECXzjK59EiRvg6BJbaOD+m58uG+LAEAAiABEACIND38BFH51Y63fvTPB+wZj7fkLJ7Q/Ekazm3LsbRPxZ8AQACIAGQAAhEEkTi6uAWgw7u/hS1c0Ytr9rJfD67NAxbMX1AMhk8nkOcFgAgABIACYBAVOEkrhK3RO8PqMN17cqdsNeqazGmD0d8xWq5AEAAJAASAAEDQWU2prtPVAhkfz63Q6CqjgbO6XMZxwcj7JcJAARAAiABEDASXOJa5l70ZaPumEPfYcUiLklQmZ+qqvMyTX8owjYpAEAAJAASAAFjISbOja7DjvchV1YHZVP2xIdAOQoG71Oue0o/AYAASAAkAAJGQ82oMr8vYK2WqzJaEvpYuRP9RuknABAACYAEQCCWkCOjgF7MD8OKktAVK3fmCX2I6npn1U8AIAASAAmAQFyhR4LOlAUPRcLfcdN7obFdA2Kwy5XSZwAAAZAASABEMkNgXNtC1CMd4+OqOkoyF9HvS+iLNsiXVnzNU8ybDMmHHKM0AwAQAAmABEAgzgAY94IwjYKElIae6cccQT3SmVds1xDFeSoGxzkd2v0W5yAM3V5K22oXC78AAAGQAEgABGwIgdIpP215yDivb+eCTnSpwe/h6XAhIS+rb/Oc4b6qDXylLq83OS9HVLoW2GH0DwAIgARAAiBgVQiMc29A2MvXoe+M3PZzBEuPPo/oMJjkIMjoHwAQAAmABEDAugAoHXBZEIYSSUjZbcuyzj5fe8dUcj+AYPQPAAiABEACIGBlCMzpEMgWCOnih6Evzn0Z9fUnI9H5BLUto38AQAAkABIAAatDoM3zAdE/Rkf5OrwGZSRQRgST8EEEo38AQAAkABIAAetD4KjugCM5fGXBKF8H16CMBsoWJS6XJDP6BwAEQAIgARBwJgTatD8gulNU1cVbJl3dfNzx63AiaPdhLkMAIAASAAmAgCudb5kPmKclnPHl/omqzyt2xnwdSgCUuYGulYTucjV4AwAIgARAAiDSGQBZGdR+shdfMThOdbsvnyPXomsLFMmo6yEuTwAgABIACYAAIRA9hwtl6QIuXItfOuTCXEsAAAGQAEgABAiB9klkaWcP16KsUpu3+GH6wTnaxWULAARAAiABECAEou0QEYa+IEwUaY5V16PNi8McDc7ZCc4SABAACYAEQICON5qROXynVHWUr0RzOHstbmPrBwAgABIACYBAkjreo4p9AvultrTTpzmcD4Fs/QAABEACIAEQSGTHe0hVN+rO0BodCefzhYu4MFKUrBDI4i8AQAAkABIAgcR2vHM6BDIvsDlf6U3ZCQeJDoEs/gIABEACIAEQSEXnWzbpHqElVoU+CXunmM+XmhB4IjjXRzkTAEAAJAASAIE0dL7zqjoa6KW4GSToyXy+SUJfKkPgLuZxAgABkABIAATS1gEfDW6OqPTMDQxX7pyk85/qEFgKzv9eWh8ACIAEQAIgkMYOuKeqq4QWEvorsnKn3ddfHHtWsvcfABAACYAEQIAgmKAgGIY+Vu4kBNZD+ScAEAAJgARAACuCoGwd4UppqIS8IqHP+RA4a+Cao/wTAAiABEACIIAGHfJCcBxWdm4dEe7Rx3YNybnm5DqbijgEUv4JAARAAiABEECLjrmnqiOCcYdBWcSlqENfkTOTyGtNrrPTEd4F5Z8AQAAkABIAAXQYBvPBsU+HwagC4ZwOfOfC4EdpZ2quMdmnciyKDxAo/wQAAiABkAAIoPcOuwRCTx97VLWEL9NGOCzpoKd00BPF4PAZpUn9NRXF9hCUfwIAAZAASAAEAFgaAqdVf0eYKf8EAAJg6qzl9AMAHLFfLY8Q96pE+AMAEAABALCUnvO5v08/7gwtCgAgAAIAYHcIlHmiw334UWwVAgBIJeYAAgCc0+OiMLKo0C5aEQDSizmAAAC45aiqrhrbjSLNBwAgAAIA4Ag9H1BKQbtZFIb5fwCA1KIEFADgrMFsdii4Od1heOQNAABSjn0ACYAAAHdDYCfzAYtBANxPqwFIooXLb8heqRn9v54+GvH1IeY2vPjTUpraKs0BcICnCgDAcTIfMKfa2ySe8k8ASQh5OR3u9ujAl+/Dz60EQVWdXy1HWW6DYFik1ZOFEUAAgPMGs1npDE2p5U++G9mrt5IAABfCnqfD3R59m4vpoUgIPBcck0kZKaQElAAIAHA/BI4EN2NNvoXtHwDYHvjkQyyZ27xPBz7Pwofpq+peqqdcDoMEQAIgACAZIXBKNS6FmggC4DCtBMCy0Ofp0HdYxTfC10sYPCmvr0EYnHPpgRMACYAAgGQEQPn0fFbVLwUdDgLgBK0EgNDXd3M6CJ5wJQgSAAmAAIDkhMBGW0PsCgKgTwsBiDH4FYKbgzr8JVElCAYhcJQASAAkAAIATIbA0ys6WMz/AxBX6PNUdauaI6r1QlVJ4QfHsM0riLINBAAAySJz/fI1na0iTQLAcPCT16DDqv19SpNEQu9U0AYngtvjrs0PTLq1NAEAIGlmyuU5HQJD52gVAKaCX3DIglRTKQ1/tUZ0EMxxZdiDElAAQGLVlIIy/w9A5MEvuDmm+rApewLJh3L7bdo2gjmABEAAQDIDoJSATjP/DwDBzwoyL3CCAEgAJAACACINgbokFAD6Gfy84GZMJXdFzyfMz99Xczfuqnv3FtWd2/fV0tJDNR/crrRh4zq1MTg2b326cpvZvklt2fK0dSGQAEgABAAAANoJflJZIHPbjiX591xaeqSufTavrl29o24GwW9p8VHXP2tg3Vr13PNb1HMvbA5uN8uX9sZdDkoAJAACAAAArcKfjPbJqJ+X1N9Rwt7lS7eD41YkP1/C4EsvZ+bu3V3c/1v/zb+LLQQSAAmAAAAAQKPgJ4FvXCV4np8EvpkL19XCvUWTdzsRHMdfHy75BEACIAEQAAAANoS/sNwzkZu4xxT8askc7ZNBCBwlABIACYAAAACIK/hJ4JOtZPJJ/P2k1PPjv75adyGXmPjBMRwEwSIBkABIAAQAAIDJ8Cdz/aTkM3GjfrK4y0cfXo1sjl8fHDcxGkgAJAACAAAAEv5kkZeRJP5usqLnB+9f7mlFT0OKwXEoCIKRbeFDACQAAgAAIN3BT0b7poIjl7TfTUb9Zi58ri76N1162L4OgZGsFEoAJAACAAAgveEvp8Nf4ko+ZQP3D9+/bNNcv07ICOD+KEJgmgPgWp7yAAAASHH4KwQ300kMf1Ly+e4vPnE1/Cl9TqbeHs8VuFL7hxFAAAAApDX8jarqFg+Jc7F8s7LYS4LICqET/fphlIASAAEAAJCu8CerfBaS+Lt98P4Vm1f57FZfy0EJgARAAAAAEP6cJou9yCqf1z67k9RT17cQSAAkAAIAACD5wU/mlI0lNfw5Pt+vkxC4q9ctIgiABEAAAAAkP/wldpuHlIS/kIwA7u8lBLIKKAAAAJBsY4S/xMjp8wkCIAAAAPCkJM/5S2H4CxXeHs+NcHV3jhJQAAAAEP4If67a282iMJSAAgAAAMkLfyMqsVs9XCb8VZ1+ezyXoRnaN0ATAAAAIIHhb0hZPE/s5o276s78fbW0+KjyZzE/v1D5/yc66+vWqi1bNqgNG9epLVufVpntm9RF/2aSt3rolBccx4LjKE3RHkpAAQAAkLTwJ4uEyIqf1owMScibu3GvchsGPvSVrApabPeb2QaCAAgAAIBkhD9rtnu4dvVOZaTu2tX5VSN76DtfVecDtrU1RJoDICWgAAAASJLxOMPfwr1FdfnSbfXppVuVP8MYLzhkzucoTdEcI4ApcuAnFzz95Ajl2/hnvj4qzv5od5GnDQAAsNHC5TcKOgAaJ2WdEvwuB8EPsdr1+nDJb/VNlIASAJMU8nI65MntHlWtfc9HcFd+zVEODll+1w8CYkkBAACYD3/S/5lWhuf9SfCbvXC9L/P6Nm7+qtoUHLXu3vlU3QsOtK0YBMD9BEACYCIDoB7Ry+ugl4so6HWjpI/z8iQkFAIAAAMBcMpkX0j24fvow6tdjfitW79Fbd/5t9TW7d9QO3b+ZiX4bVwR/Fa6ceXfq19d+GP12SdTavHBPCe8uZYLwhAACYAuhT5Z0nhfcMit59BDlyfhOR0Ii7wuAQCAPoY/mftlbMuHi+WbaubC5x0t7CJh74Wv7w+OfOXP3ZLw9/M/+V11+8YvOfFN+p2tRgEJgARAF0LfQR36krDR5ZwOhGd0IPR5nQIAAF2GP+kbzZroI8mo33vvXmq73FNG+l7a/ffUrm/9qOUIX6ch8M//6B9QGtpc01FAAiAB0MbQ5wU3R4KjkJDQ14yUiJ4KjknCIAAA6DAAjuv+UqQk9L03famtUT8Z4fOC0Pe1IPxFRUpC//JPfpcLoLGmo4AEQAKgTcEvH9wcU/bM5zP+ZK0Jg3MKAACgcfiTNRCmo74fmef3wftXWn7fjp1/S72S+0eV+X0mSCno9SAIoqGGo4AEQAKgDcGvoIOfx3O1QsLfZHCcZBEZAADQIABGvvBLO+FPyjsl+EU54lcPo4AtNRwFJAASAOMMfnmV7hG/tp68wXEqCIITNAUAANDhT/pOU3GHP+9b/30l/Ml8vzhM/evXmQvYXN19AQmABMA4gp+nqqtVDfG8bJs8eY8rykMBACAARjz6d+3qncqCL41I4PvNH/xzY+WejXxc+v3g+D+5IBo7EQTAowTAZWu5JmIJf7JU8TThr2MSmmWi92zQhqPBkaFJAABIZfiLdP/jhXuL6oP3Lzf8e1nkJf/fvh17+BOyrQSaKtAEBMA4g58XHPJplYz8EV66J213TAdBntQAAKTPkSh/uJR9NlrtU8Lfb//d/yu2ks96jwfN+41vj+foLxIAYwl/Mtono355WqOvQXA8aNtZPZcSAAAknN73L7IOvWzy3mifP9vCX2iHBSORljtIExAATYc/Kfk8rRj1i4oXHFMyuqrnVgIAgOSKLPxJ6efMhc/r/p2EPhvDH9oy9PZ4jn44AdBY+JM5a2O0hBH54JiW+YE0BQAAySOd+MUHDw9H9fOblX7Kgi+2hr/tjAC2FQJpAgKgqfBXoCWMqswPDNpegmCO5gAAIBHBLxcclYXg7ty5H8n7u6z62aj0U7Z6IGQ5jzJQAiDhL+HkzWFal98CAAA3g18+OGQBvWndr4qsjO+jD6/W/Xq4ybvN2AewLZSBagM0AeEv4caC8yGf+Bxi70AAAJwJfuGK30Y+yJUN32X+Xz3f+s7/bP28PwJg2/LBMZn2RmAEsP/hb4TwZ+WTfZaSUAAAnAh/lSqeRuFvaelRX+9Pft5Hf11/9E9W13zh6/utb7PbN37JhdOefTQBI4D9Dn8SNJou+PJocVE9XLhfPYI/P1pcavoz123aqNY8tVY9tWGDeurppyt/Rlfkk0QpCR0++6PdEzQHAABWhr9CcDPe7Hvu3L6vnnt+c9/u86J/s+HCL9/+L49b32Yy+rf4YJ6Lpz15moAA2M/wJwHjdL2/W5y/ox4Ex9IX9yoBsBNLXzw5GXntunVq4JmNQTDcVLmV/0dHZN/AfUEIHKYpAABwK/xV+lVLD/t6v59eulX361/b/fcq8/9sd/3Kv+fiaZ8sJpR5fbiU6mlBBMA+BgtVMzFZgt6Dudtq4cZN9fhh/0oVqj+3+rPFUxueVk9ntqp1WzYTBttXCEKg3B5lXiAAAFaEv3w74U/ICGC/NJv7Z/vCL6FLF/6YC6gzcq2leh4g9YR9oEs/h8KA9sWnV9Stj2fVvWvX+xr+6pFS0rtXrlXu7/ZMuRIMo77PpIRAVd08ntWgAACIN/w1rKKqZ35+oW/3fbF8s+7XXRn9k/JPRgA7lvo1IQiA/VH5xGohCHxhCIuDhMFK+LwwU7nttNw0pS8AhEAAAOLvR7X9Xizz9RqN2nVifv6+mm8wmujK6N/Hpd/n6ulc6heCIQD2KAgPhSB4eRL8TIz4tUMeg4RQGRW8c/FTtXT3HieKEAgAgHV06edQvb/buv0blZG4ehpt2N4JWfylHln105XRv19d+KPYH8eDxccu9v0IgOje/Rtzx+bLFyujbzaSBWjm/YtqvvwrgmCLEEgzAABgXN15f7Lv3m/+4J+r7Tt/s0EA7L1Pc+1q/ZUzv7b7d5xouPf+/JgVj+PG7YeuXXOZtG8ITwDswfdG/+343StXPRfm3MlqohIEKQ1tHAIP/OTCOM0AAIAZevTPq/d3sv2CjMLJPnz1A2BvI4DXrt6pu/WD3KcL+/75H/wr5v712O9L8y/PKqBdeu3Ns+OPlpYKrj1uKQ2V4+nt29TG53Z0vK9guIehhMil4Pbxo0fq8cOHDUdAwz0MK582rBtQT61bV1m5dK2+tYysDlo++6Pdo1zhAABE7nC9L9Zuvi6BTA4pd6wlcwDl2LCxuxXQr312p+7XXdn0nbl/fQmARQIgOgp/qrqKpLPu37ipHty6pTa98Lxan9na8Psk6EkZ6eIX99TS3bsdz3GU71+5l+ETF+Azmyqb3cvtQHBrgWNBCCwFIXCSKx0AgEjV7UutXIBFAmG9uW4yivdydltXd9xoBNH28k/Z8P0//On/ZNXG7zduPVQ7dzgXKSgBRbrCX204k5JQmR+4sixU5gvKAjKykIxsMyEhMIpSVwmHsniOlKfO/fJC5fHIfcVMNov3uNoBAIjG2+O5hgu/bF9R9vnC1/MdhbhWZPXPequIykij3L/N4e/nf/K7q0ZDY39c7i0CI/ak+fnHCGBn4W80KeFvZQiToCcloTISJ4Gs2ahdlIE0LFGV0tEN27dVRidj2OA+3I9oL1c9AACRqLsUf70RuO0N5gFKGefS0iM1MNDZeMZcg+Boc/lnGP6k/NM2D9wMgKkeASQAth/+JPgdS/LvKMFPyWEBCYPyeOSQECilqp3OV+xRbv/YO6cXrt88r6o14nPvvHWgxDMBAID+vM/W+2K9sCcrgkoZaL1FT659Nq9efOnZju640cjhjgYrjhL+mnNwFVACIK8/bYU/eZEaoyUae3XX9rpfv3zznro819tSzTIiKGWhMkIpi9eYsnbdgJSnDIXBP7gOlA6DZ4JjMgiEPmceSKVCcBwMjpMqxYsIAFEEwEYlmFIGWjcAXr3TcQBstPl7o5HGOEnok/Bn05y/Vf00N0cAWQUULY2n/ZOC2qC3d9cO9crOLerFzEb1yotb2/6307M31PzCovr4ynzw5+vqo8vz6s5Ce1tSyIigzEV8MP+F2vy1rxoZDRzYtKnel/P6GAsCoXT8jgdBkA4gkJ4O63hNx0E+IJoIjqPBMUfzAB1Z1a/a0SSASXnmB7/4Z6sDYBdloI3m/8lIo01kq4d6v7NtZBEYEAATRc/7S/WnBBL6Duz9mvr+N59Xmzd0Px9vrx4l/P43X1Bq/+7Knz++fFu9699QZ6cvVf7cisxNvD1TVptf/mrk20jIz5eg2WTxm0oY1EHwKCWiQF87hmHVxXHpB1nwmOS9oN40gIIOgvI4T3DqgNbeHs95nf6bcIGWemWQnZSBNir/tGnxFxntk03eP/tkyvpzKaN/69et4aJ2DKuANg9/OZXweX+tgt+p/+F76v/4h78dBMCXegp/jcgI4huveZX7+X/+cV79+AevtLwfWbF0vnyx4d6D/Q2BG9r5NgmC0/rDAgC9GQmOWR2sCvrPoyq+KoxwUahjbQRW6a3lOIVAS3UDYKsSzEZbNEgZaLtktNDmACjbXRT/9etOhD8h8/+2P/sUVzQBMFFSO+9PgpgEv05KPHslJaU/3r9b/dt/8rfVkQPfbBoEZVRORgJlfmCkAfDpjkYZjwUh8HRwUC4MdBe0pvTr7srnkISvaVX9sMV0J1Ue01Cb35/Xj3OU0wn0X6NVOqUMtF5ZZz13Gsz/27j5xdiD31QQ/GTkz+b5fqsCIOWfBMAk0at+5tP4u8uI3I91iWacj+EP//G+ym0zsm9glCFwbedzDaWjOEUIBDoio2azLV5zwzB2WpkZDczpMNfNiN6xHv4tgAakDLTRPMFORgFtIfv5fVz6/S+Dn237+7Xji7uPuDAdxBzA+uEvo1Jc+vnjH+y24nHICKCMBMoo5ImzHzZcMEZCoJDtIvqty3mGOd1J3c+zCWipoOqP+jUypIPicHBMRhj+pnoMmuHPYG4g0Ecv7f6duquBfuLfVC9nu18pXAKYHBIwpRR16/Zf6/vG8DKydyN47Nev/IfKra3bOnRCSkDXDzAHkACYDDIHxUvjLy7z/qKY69cLmX8oq47+3h/8wngIXPNU/bp2WchGtrdosnCNLA4z9s5bB47ydAKahr/xLv5dOC9vUgfBfq7A2Y/wV/s4Jdzui+BxAi7z64aJSrD7R03/oZSBrlv/z1aVSUoJqCzwsm37pqb//l6LUtHrlYD2ZMCUILgpOLYEYTBcKbTVnoF373yq7t25XHmc80HQq/7/p4k7kVIC+q3Bp7miCYBu06N/R9L6+8sWDzaSUcB/8Q+/o946/X7D0CUhcO36dWpg00Yjj+ef/uhV9dYfvldZwbTRBwnB9XQuCIGTPLOAvoW/WkM6sEm4KloW/uo9zkPBwWrBSL3Xh0v+2+PdVUhLAJMQKHPmVrp86XbLANiNezq81QbDjzmN6s7dR67uAZh6zAGs02lXKd7z71Vvu7WPLQyBzRamuXPxkpHVQUNv/vDblaOJMeYDApGEv5CnQ9tojz8nHFWM6vkqj3Na/+4A6minJFK+p9H3Xb50q+ViMBs3rqOh+0TKP8Uzm4gTBED3HU7zL795w4Dlj29d0xAoq4Peufhps737+k5KVJssVuPpDxUA9D/81Tqmuh+9C1cg9Qz8/uMR/f6Aa4orvyDlks1WwJTg9/M/+d2mQbHRPn+hF1/aqn7tm89HMlKYNjf1CqCbCYAEQJfplT+9NLeByW0fogqB4T6BJsliNa/uajh6eoRRQKBiKOLwk1fV1UQ7rS0bU2ZX7JT3mmmV4moTQDWYBzjfINxJyeef/9E/aBoQZTP4VhvCb9i4rrJYzKvfeVn913/3G5Xbwd1fIRB24cr1pcoti8AQAF13mCZwg4RAmYPXaMEaKQO9e+Wa0cf0T3747UaPRzp5jAIi7XLKzMhXRnVWajmi4inL7GWbCSAJztf7oqyQuZJslSArdDYjo3rf+o2dHT8ICX67du/4MhB+53ue+varL1VC4XMvbFZbtrLAScMA+Hk1ADq6EXwxzeeORWC01948K2/CeVrCHbJxvIwENlod9P6Nm2r91s1GFoUJH88b3/XUv/zTjxt9uDDKWUNKhSWWJke8JGyGq282Iq/5YzG2i6fbRbaMYXEYpE3dDvhnn0ypV3LLK4FK8Ku34MuXHdl1a9Wv/RfPtxz5a9eWLU9Xjuee37zq78Ly0qWlR09sKH/t6ryav30/VSfvy9G/dYz+uYgRwCc76HCMlIG++cPfaPj3siiMyfmAb7yWbTQK6L325tkhzhhSynT4CxWa3He46IsN4ZjFYZA6rw+X5EOPVVujyPy+cC6glHy2Cn+vfufrfQt/rchooRwSDmXUUI6vvLA5deGvEtTdHv0TPgEQijffqunZG849ZtmT78c/eKXu30n4C/cINEHC3+t7X2r01we5wpBCpufXrZRvEAKjXPGzG+O8DyGFivW+KCWfrRZ7kdLM3/6uVxmti4uMBL737qVUnrhwBHDzRmejRJkAmHJ6ZIbJ+AHZ3NxFP96/u+EiLIvzd9TSXXO/14HGAZARQKSNXPM2zH9dOd9uRNlZ8k8IRNqcqfdF/4N/1TT8ySicjPxtiHlLh48+vNpy24nEBkA9AujwCqCpLrsnAFYxMqM12mTdBU0WYVFfXOpuFPDxw4cd/xspS5X5gHVk9FxTIA08Zdd2B/J4pnTAGrO43QiBSJPJTv+BlHvKgi0DA/F2YWXPQTnS6JMry6F3m7sloHMEQDAyo/3Zh585+9gldDWaDyhbQyxcu97xz2y0qXyDgPclKUttIM9VhpSQIGNbZUVGubEHHyEQqfD6cGmukxDY7Uqf/TY/f1999NdXU3vewvl/wtUS0ODaKxIAU+y1N8/mFeWfX5ISUBfnAdYGr0aloAs3bvZtQZhWAXBv4z0B93CVIQVGFR92EAKB9pxq9Q2y2IsEP9m/L24y7+/D9y+rpcVHqT1htSOAji4Ck/pVlxkBpPxzlbenf+X045dS0Hok/MnWECY02RTe4wpDwkmZ8zGagRAItOP14ZKMAPrNwp/JlT5b+SAIf2lc9TN049ZDdefuI5fDHwGQAFiRpwmedHb6krOLwQgZnWu0Kmino4CLDRaP2byh+RaaMhexwXxErjekIbSgv+3J3GEk3fF6X7Rhpc9asxeuq2uf3Un1ifrPFx98+eftW50NgOcIgCn22ptnM7yx1ve//eF7Tj/+RvvxSfh7cKv3Sduy0Esrv/biFi4kpM0Ir6mRmKJdkWSvD5cm1IotIST82bDSZ0gWfJm58Hnqz1VCFoBhBDDlv3+el9363p29URkJdJWEvze+69X9u4Xr7S/89OjBYk+PocEHD3TkkETyhKP0MxrhpvXMV0eSHVV6ZUYp9/xO8B4e90qfobQv+hKqLf8UO3cMuPhr+K8PlwiAKf/96Yg3ceLsh05vC9FoFFBWBG13X0D53pXaGf1r8X104pBEY1zbkQfsKZoBSSWd8sHdXzkaHFas9BmSff7e/cUnqV70JVRb/ikcnQNY5NlGANzHJdDYnYVF9b/85N3KrYsk/H3/m8/X/bv7c63LQBvNFZRQ/D/+wc+dXi0V6LO8YjsdE+RDS+ZYIpEWLr9R2LV7x1hwWPOYZMXP96YvEf60CzUBcOdXBlz9Nc5wJgmAjAC2IIvB/N4f/MLZEPjGa17dry/Ot57E/fB+41W+pET294IQKEHQ5b0TgT4hlJhTUKwMiuSFv1Fl2d6hEv5k5C/NK37Wkrl/DxYfLwfAHc4GwCJnU6mBtP7iegEYypXaICNeh//Fz9Q//dGrbZc/2hJef/qOX/fvZHRPNnl/akPjlcXamf8nQVCOcOXRA3tf4oJB2sjCLx7NYDxw14Zumc8yV/PnW/r/SzW3gI3BL6OvZesqCN579xLhr8Z//uTJ8s+Xd65z8deYfH24NMfZTHEAVIz+dRymZCRw5MA3rQ858lj/5Z9+3HIRGxkFbBYA165fp9auW1d3HmC9+3zrD9+r3C9BECkinTcWfrHr/Szf4HvCIOgHR7nmz4RDxBX+wpJm6/pjH7x/Rd28cZeTpMnCL7Wrf65ft8bV+X+UfxIACYAdvwAsLFZCjpQ8vvnD32i4ymVcZKRSRvzaXb10aaH5J3sDmzaqZ1/ZVQmKCzfm1NIXrd8MaoPgi9s2ctEg6Y4pKilcCuuNwmFRB8FyzZ+BKMPfkLKs5LM2/MmWD1j24cyT/SVHyz/n1ig1ydkkANJp6ZIEwB/+7zesGQ2UwHd2+leVUsx2rduyWT3z1Z1tf68csnLovWvX2w6CcjRA5wpJ4Klq+Sfcl68TDiUIntOvV/JnyqbQr/A3ZutrB+FvNZn3d2HF6p8vv+hm+ecByj8JgIE9nP7uhaOBcZU8ymifBL+3g6OTBWqk5HPTzucro3sdP1mCf7Ml+7WOgmA977x1gBcgJAGln+kKhWEQPKNYRAHdBT9PVfeztLICi/BXn4S/2sVfxNfdnP93nLNJABSMAPZBbcnjf/ddT70eBMGoSkPD0CcjkE1G1+qSuXwbn9uh1md6X8QmDIKyiMzCjZvqwVxHeyUy+ockkI5cgWZIlZw+wpGbyZow6NM8aBH+rC35lNU+P3j/srr22R1OVB0ryz8l/MkcQMfI4i+8ThEA3QmAj5YeqLUD650IgifPflg5vv/NF/TxfE9hUALfx1fm1buz14PQd7WrrSj6GfxWktFEKSOVny8jgm0GQV6AkASM/mFILa/cKB9sndKhkNc4rAx/1pZ8stVDczL6JwvA1HK0/PMkZ5MAGGIRmIjICF24N55sG/HKzi3qxW2bKrdbGgTC+SDcSdi7fPOuuhKEyXd73GQ9yuBX7746CILnuELgOE8x+ofV76dyjNWEwQnFvMG0Bz9rV/kk/LXn/C8XVn3NwfLP4uvDpSJnkwDolKV782r9lh3OPv7KKN7l28buTxZr2bBjW1dz/PoZBBeuz6kHt25V9htcgRWo4DpG/9BuGJxUyyODSFf4G1EWrxI8P3+/Ev6WFh9xshqoN/q3++X1LpZ/MvePAOieteueVksLd9TAhs00RpPg9XRma2W0T/5sw+PZtPO5ShC8f+NmZZ6gDoLFd9464HPG4DBPMfqH9oVlor5aHhXkNTDZwU9eI2TUL2/rY7x29U5lzh/hrzFZ9OWv/uPqtRYcLP8sMfrXoK9KE1ie0IPgt3DzMg2xwpqn1lYC3+aXv1rZq29DELZsCH8rH6M8rmd3D1bC4DNfe7F04CcXWHwILmP0D91+cCDXzqzt4QA9hT8Z9Zu2+fxeLN9U7717ifDXgiz8snLlz82b1jpX/rmGuX+N2+bx48ep/MW/+7/+G2d+8dsX/5Pa+vKvc7Wq3rZxsITMiZEXpBNnf7Sb+TFwrRM/SzOgT4pqeVQQbgc/z/ZgL/P9PvrwKts8tEHKPv/43PyqAPhbf3Oj+tbg0y79Kv7rw6Vdzb4hrRlIMALoAEYBl8nWCw8XFlz+FWQEUD4Jv3ngJxfGg4PFiOCKAk2APsrr0DDLteV0+LN+1G/h3mJlvh/hrz1S+rky/Mm8P5n/55I11Q+YQAB016bnsuqLa2UaQrt75Zr64tMrSelQTwchcCo46ADBZvLBxRGaARHwCIJOBr98cEjwG1MWb6sl8/1+/hc+K3226cr1JfXJldVbbsnIn0uLv+hHeoIz2hiLwDhCFoJxZU9AE2SrBRkNlDmAts3960JejiAEyshgpSTq7I92+5xlWKSgHNk7Fc4HQXkdlFX7JmgSK4NfRoc+68P6R399VV30b3LSOvCz6burvibB75tulX6KiQPDJabZNMEIoCOeeS6r7lz+mIaoIQHw9kxZLd29l6QOUGWhhCAMng6OIc4yLMHoH0wHwSnFYjG2hT8p97R+pFa2ePjFX/iEvw7Jnn8rt30Qjo7+Uf7Zqp1YBMYNMvp36een1cvfe4Ortg5ZZVNW3EwgXzEqiHjJBxGnaQbEZEJVRwR5/Ysv+MlrwJgO51aTVT5nLnzOKp8dunHrYWXhl5Uk+P39v73VmQCoH6V/oMXiLyEWgYH9J2pgfWVDeBaDqe/etetqvvyrehuvu07ecMNRQZkvWGArCRjG6B/iVFDVRUZGaQrjwU/m+clI7Gnbw191oZeLlZU+CX+dkQVfpv7qi7p/Jyt/Ohb+BFs/tNNejAC6Q7aDkMVgXnz1AFduowv6qbXqma/uVOu2bE76rzoZHGfklu0kEPEHEGz9AFuUguOoqm4hgQiDn6p+8Jh34fEy6tcbmfd34eKDVV/f/uxT6nf2bXEt/IldB4ZLfjv/Ls0jgGleBEbeSJxagl9WA73+0V9WFoSRrSFQ58n88JG6c/HTSgCUICiBMKGG9CFbSRAGERVG/2ATec+WESlZ3U/KQnm9S3Hwk1G/D96/om7euMvJ65IEv3rhT3wvt8nF8FdsN/ylXZpHAJ2cYP7Ze/9fpRz0uW99n6u3BVkddNPO59IwGlirVBMGS1wF6IGUGs8qVv+EnaSTN6wYDexH8Cvo4Oe58phnL1yvjPqhezLv7//9izur9vwTuW9sUHuCw8EAOBwEwIl2/y0jgOnk5CeHshrotQ/+TG0bfJVRwBYeLS6mZTTwiddtfRw78JMLc7pzJIGwyCIy6NAQ4Q8Wk7AiH+TKSOAozdFx6JP2kxH+gkvPcxntk1E/Gf1D9yT0/ax0t2742/mVAVfDn5jk7LbZdikeAZQ3jGPOhZqlB6p87v9Wm198hVHATi70IPzJSqFPb9+W5mYIA+F5fVuiZBRNTCvHyuSRWlLtcEixUmir0CdBb0gHP6ee2xL4ZF+/a5/d4UT2gYz8Xfl8adXXXVn1s8GjmzwwXDrUyc9hBDC9nWHnSPmnhD/ZE5BRwA6e5A8fqbtXrqkH819UguDApo1pbIbwzV+OyocfB35ywdedp/O68+T3Kxjq1UrDTka+pqM2F/z8Ilel1TzCHxyS0x9YSEkoIwD1Q99BfeuUpaVHlf38KPfsH1n0pV74E3/nu5tdDX/iDGeXANgOZ+dHhZvC35x5l1HATt9Mvrir5oNjfWZrJQjKPEE6+pVjaEV4+zKs1TxfbrX4WVm1PIck3yIcys89GQTBUa5KK7H4C1wjQUe2K5AFYo6mPPTl9WvwQeXwBzkyz++T8g1W9+yjD2buN170Ze+mysqfjoY/wYc/nbRliktApaPq7PLmF3/208pqoLIxPKOAXV78T61VG7Zvq5SFpmR+YLzh++5dtfjFvUpbr9+yOQzfJ4IQeJTWsc5Nxfw/uKuoqiWhiS9x12FP+jN7dNjLu/47Xb50S80E4Y95fv0lwU9G/xqFv90vr3c6/HVa/inSXAKa2gC4Zs0a9dqbZ53t5MzNTldGAJkLSBB0wd0rV9XCjZtPtPnW7NfVUxuelv/dxlxEq8ho8GmaAY6TqoVh5XC1z4qgN6QD3h7db8kn7YQR/Ah/XQS/0NEgAJ4gALZvIOXPiZKrL6IS/CQASinosy//ulq/ZQevcF2S+YH3rl2vBBSCYP/Jaqy14W+5zT9Xm19+SelOTZGWssZBmgAJEO4ZeMjV1xc9f29MJXxFXoIf4a/H8Cco/+xQ2nu5zn4yKGWfsjG8uP7xz7mS+xgEb12YUQvBrfw/2m+7B/N3Ku13f+7WqgBYj3w/rCOdzALNgARdz1MuXtNB+JMAO6sc26ah0+D3s3MzbOsQQ/iThV7+zvc2Wxv+1nQW/nw2f+8iR6T89z8XHCOuPngZ+bt7rawWbl6u3IaBEP0JgjJqJXsIslhMYzKv7/7c7VWh78Gt22pL9uXqC/na+pPKdfkn7DJEEyCBxvXthCPhLwyuGdn6QFbBFBs2rlPffvUltWXL6tdO2R/vy47duqfqfo8V7xl6VU8Wd4kv/MlCL/t/6xm1eZOdY0BdrEHK6B8BsGNOzw3YsO3FykigLAZz/aO/JABGEAQfBOFGDgmCG3ZsS+v2EavIqN4Xn15Ri1/ULyup/boEvXXPbFr1vRuf+0rlli0hrEL5J5IcAmX+nAuLTuUl/MkqmGH4qwTDe4vq3V98or6372+ogYFq531+/n7la/XC1LbtmyrHV17YHHsglMcuZZ7Xrs4T/AyQ4Fdvtc/cNzZYu8l7D5tPnOOMEwA78s5bB/zX3jzrq+Wl650jewFe++DPKiFQFobJ7NrLVR2Bxfk7lUNGAjfsyFQCYRpHBSUUy8iozN/rhIwGyr8L2/DpzNYgTG+SUtsJri5ryOsgI4BIMqn4kdG1YcsfZ2XrBglLK0l4mr+9UAl2YvbC5w0DlYwKyiF76A2sW6uee36LetnbZjQMXrt6p1LqyQbuZjxYfFwJf59cebKkdudXBtRv/fpGK7d56MOug0XOPAGw2wun4OqDl8VgZPTv0dKDL1cFZVuI6MjIl2wor4JDQqBsZyB7CqbBw4X7av7ipYZz+p54Qa+ziI4ssCPHlz+r/CvZl5GNW+1B+EMahO/3NofAtquT2h1Nk++TICbHcy9sVt/e+1JkD15G+yT4feLfZG6fQTduPVQ/K92t3NYGPxnx27nDru5+H7eaLx0YLrGKOAGwK2eU44sePPv1v1kJf0JGA1989QBn1YBwVPDuZ1e/DINym0Qyx09KPtu1Yfv2hiFSRgKlrDYw985bB6jdt8dhmgCEQCsU5T8yYjd/+/6TnbZ1a9WWrcslfBLmauf/tUNG46R0tJ8jgRL05HFcvnS748eD3smIn4z8yQigkMVd/sbX1yc5+D3xXAEBMJUXz9aXf13d+uQ/VkYBZUGY2xf/U+VrMKN2rqCMfCUtDIbz/doh5Z2bdj5f+f1r20eC8v1bt2XEr/bbCX/2CPcYA9IUAmXkwLo5gRte/OncwuU3Jnbt3lFYXHq4ahGYcP6fePGlZyslnu2MBIZloIO7d1R+Vq8k6M3duFcpVV0ZVGGGBL7zv1yozPeTsPfyi+vU13euq6zyGbctW5+uXG+Z7RvV+9OXopr7yfy/bsN4mjeCD7325tnTyvHyp3Bj+EonfGC9eum3D1EKaoEwDA48s9HZOYPhnn0P799vGPrkkN+zdmVPCX0P9Chpgy019r7z1oESV0mswn3GCjQFUkpGASdse1CyEuj87YXZLVs3tNwCQlbW/OjDq5VAFpZcVkYKt2yoBD3piGe2b+ppxE9+rowa3gmCXji3EPGTkb/NG9daMbcvXHRoc3C9yW34QYWUHX/4/pXI7raXEtA0bwRPAKwGQOn8jLv8+8jo38Wf/bRyK2SFUEpB7SIhSQLhuiAMygIoSdtsPhzpW7x7t1noC/lB+NvFVRGrnH7dY+QPabdfWVgN9PZ4bigIb6fDURQp/awd/YuChLylxYeVkT0ZfZTANz+/wMqd9jn++nBp9K/+zX+V275j05FHjx4XKgsE6XN1LwjsUcy/lA8UNgZHeCthTz5YaDaiPP2Li1F9YCD7//XUj0hzAKQEtGrS9QAoo361cwEpBbUwpC8uqvs3blYOIaNlEgQH5NbREcKlu/cqZZ2L+rYDp7giYlVQ1ZG/DE0BVN7/ZQltqxaTCDr4k0EIPDF/+/4T+xWHK4BK5/v/Z+9dwKM6z3vfF93RBYmrBRgYEeEYHIywHYyT2Ix2kt1E2A3E3SYliS11x93uSVpD2u72STlBStk5T9JkA6fuSXaSHuSdhMfOsx3k2iJNTxyGeMcXNQFhYuMYbI2QhTAXSSChC7pw1n/NGhjE3Nd9rf+PZ54RuszlW2vW+n7rfb/3zc+7FvmBJCZjUJW7yRjZuyZ2jOi5BuyjG5V9Q71g8cFPvogsmoaRnk27JcEFvajURxlR5XA86ZNg34q92JDtxYfo2lCTCHF3oADq4uUddf33bNsPCXR1GmjsWkCA6qBFFZVSUDabG9mBoCAKbtHESkQEc4uKJL94uiqHuDlJCiGw0dechfBNpZl7gG1A/LZwGAi5SkC5bRdn9ghs0uYmgeg3ohNqSpvvgOzVro+T8lg0/+l2RQJrNQm8bi5rZw9IVIM1kSPcJbKHKaAaXkgDBYM9x9VKoFEgf0gFRYSQuHA/1aQwt1ARwoK8q1+bnT6KyN7k5TFV+iB7EyMjqVI6MyH08o66Wm5dy0G0D+udgxwKQuLi1FRQRHUOc/P4GgQpGtansd5NEUHH1LVA8RcTe0DW1mmR0GzhGkAKYFQC+8QDKVFYC4jG8FGK5y6Rm27/GA+fHiOvpFim5eSoKaTR/8cSK4qQt6lFXKKCByB5wGDRS0SDIoDN3IKWwvV+hKQmpEmg41AksFEiUUriP5oV8Uu7ZQkKCCl3B+w+3qM40a9+cdy0x1fkT3epUwogBTAqgJ5IjcL6v55D+6/73uxb1nI9IHEC6P03k8NgufxhMsD1foSkxpFRQE0C8TkOchNR/tKQwIBEosa2HfeR/nn0ULdZD6+7AIzfBTCHn63r2O2FN4EKoIj6xYL1gBBDQuw+mXEILKXe7kkAIS7DyVE2iEA/NxHlL+U8cP7TYW1/sY1+c9eosoUUBdA4Xt5RF/bKBBURv6nr/t577RdyeeA8NzSxk90cAkvlbw+HgZCMCEpMwRUnociA7ZN64nz5i5FArBtssesNmFykiAVgKICG44ny9GgCP3PpHdd9D9VBzx578WqVUEIsJqRdZCHms5PyR0jWPO7UF4bWEMrdLm4iyl+aoLKt5VFjrP9DD0kTYQSQAmgsygQ1JB7pLYI1f0gHjQURQKwPpAQSG2DvP2uA+LHNAyHZ4/SWUE2cAFP+0kFLBbU882bw4ojZT8FUaAqgaQdXTzB3xX03pIJCAmNbRRBiAWFW/rRM/uo5DIToIuBkCdRaAXA9IOUvXRAxDlv5Rvp6h019fL3tHwgFMC5aFNATk1WkgmI94FSGznZSAomVMPpH+SPETaxz8otTRKFduB7QS+wySf4QBcSFAksDG4MDpkYAw9xdDPADDkFCmrwymSqdv0wuKcIH6bvuA9oT6c+CKCEhJoKTjylrVp5ZX4vqlmhzEL2Pd6JQbw+2HvDySWMn5Y8QfZSXlcjttyyV8tISWXfX7Rv+bNMDu0vXPODY4wbWA7buqcGxlSnf7gYN3pvNfAJFAptHejbtFIsqQg+Yu/6PAmgA7AOYhHu27W8UjzRexZo/rP2LVwUUgkgJJCbS/PKOOkOubCrCF5BIahauzgczPJltVSTQi8UTIH4s+EJIBpK3ZP48WTz/JuXrKvV7996xMt6vNykC2Oj098T+gJS/dFAE0LI57S//9femzinqDIqW+rkPICOAycFk8RFxaEnoTMA6wLnL741bAIaRQGIyulJPNOmrN+Cz6MWiCZQ/QhIA0YPgQfTuvfMDcvuyparsZcA6l7zVjRLp9xngVqf8pZjTmi6AJvf/A53cdfTDCGAK7tm2P6jcHfDK+0YaKPoBxgPN4+MVjSFEB1lH/xTxw2cP5dgNKcbwYOuBaR4b2xrt2MQm78T3RKN4kD7IXoKIXsaUrnnAFceN1j01PB64ByyLqNXWcVrKSM8m09eK93RfkGNHT5v5FBvrIu1QdMMIIEkICsIoEtgizi8LnRZRyYtXAAZyiAjh/DvqKIHEKDIuP62JH65SBg18HV6L/lVwskf8zr13rpT7161VZO8DqviZwWDbc0FFAkNOHwvIhCKB6PnGjABnE4bA2CF/Gk+aLYAjw+NWCDShAFoCIhi4uhbwwpvBmr/hvp6rqZ+xYI1g96v75KbbPyYFZbO55Yke0Pg97ZOcVtDFrGImYY+NLeWP+A5E+R5QhC8ifSszTefMFpz7Q24YH6QTKhKIecp27i2OBOfDWq2Nhy0UzX86NNKzKWzmfNbkCqBePJ/bAttApIEyiY323PEMiAJCBOMxPjKoRgKnVg0lJEPSXvunyB+q2HWIeVcmj3hoXPdI/IqnhHgSCN9T//B30v3CU/Ldr25R/2+R/IFVbhorRS4axSNtrDwG2jystlP+YjC1LdP42KSpL76uoZ0CaACMAKYvgUgFRXrFTi9JIIgXCUShGKwVnLn0DqmoWs0dgGRKi9ZPM5X4VWhCozfFOiyJrwoGxSVX8NOgXtjugfgAVOn87P0fky9+5g+tlL14uO5iC/rJaZHAIPck24HwbbW42Esq8FpMixIPmBsBZPonBdAWCdylSOAqL03Akkkg6HvnkJouipRQrgskGbA1DfkzsmgBJjtPPth6oNHDY4rx2sldi3gZrOWD9H32/o866XNnCNr6ZpEb+5a2Rye2yjEsZNDTbdSOr8wWsA9s1wYb1/vFpWj+0+GRnk3tZu0bJkcA27lbGQOrgGaIIoAVXjyoXux6Xc6/9UrCn6ttJBRZRBEZQlKQsvKnMhGqF3OKFWDytFGZRHntKqEnjzuEREHE77vbtxhWvdNgVpeueSCjieeUnqWZ1hDo1ya6B3FMy1YKW/fU8LhhH01aOq4j0ZrCbzH6cQcHRqXt12EzX3qorqG91qgH83MVUApg9hLYIR4rwoA1f6gOOrVPYCwzFt2mpoUyGkiSTFxWKwIYTjIxwknHzEiWutDeYxJoysmaELtBeuc3tz7qpIhfPDYqApiy7HyM9D1ignTh+Z/FfSbHNkqg5eDch6hfyMkvUhFA7A+HDZ8A9A7JobYuM1+6YU3g/S6ALAKTBSgKc0WutHjtfSG6hxYQyap/IlKIKqEsEEMSsDuF/O0R89MY1dRSbX2hFwhS/ogXQarnGy3/7HT5k3TkSTu2dWjHNzNkC2KJ5+jDc8WkkyZFKzqCiAlT58wHUb8qp8sfKJr/9NW0YyMZG580+6Vz8kkBtJ1nFQn03JuC/C1cs0GN9CUCVUJRIAY3fE2IRliRv8YkE6RMWzzgBLVLItVEm7Svwz6TwGiRHEI8A9I9f/bdr8s3vvyo3QVe0n7JafxOwMLXU68d33BLWUCLEmg6EL4qJ6d8JsDwQMbgxVHuDS6BRWD0feAFEjhNpnnuzc2+Za2UzF0i54+/qvYGjAeigLghJRTCyLRQ39OQRP4wYUk3ioWTUtODrQfiTVa2ale+07nKHi2a4uYWLtvFI/1HCQFo4fA/vrrFLeKXidzhIlXQ4teF5wsqx8SQdswMJZPA1j01kECmgxpHWCIVPt2aEXZQ3FfUkBcxDIJrAHWwdlvrPtHK13tRAqOgQiiqgSaL9kH+yhd/gCLoX9D2YWMC+Ut3rQGuUm9Mt+CB8riNkl4p663KY+5y4ZgGtckaIZ4AET+kfbpxol+65oGqNI5JB8Te1gst2vEunOgXuCbQEJzY2iFjRno2BSSStmwYx46elp7uC2a+7No6A1NsuQaQZMuzV3ci8e5OhIbxiz68Sa0CmldUGvd3UDgGktj166elv+Nw0kIyxJMnw4YEE6KKNCUGV/WqMql2p7V8aEjz9bkNpn4Sz4BoHxq5u1T+QCDN39tt8+vEBenDydJCEQlEQ3Jhs/hsz3WI9Fa5Xf4A2kEYfX4cGR7jXkIB9AXXTVa9LIGxIoiegInaQcSKINpKcI2gL2hAYaQEP9snqavlNisytzqbqp3K3zQnkUBI5Wrtd9zGFmHqJ/GI/P3sO19XUz/dzGDbcyk/j8qxBhG4cJx5AqShVruZfUEKx9t9WHOdbA30+kglxa3cQ9MirI2Vus5PW1PpyXmsS7YFMQCmgOpk7bZWpLbdkErh5ZTQWNkb6euRS2c75fJgb8K1gpDFMkUe2UPQkyTs+ZdmiiZKmm/U+yLi9BVUi8e4tBUEJpod3LWIV+QPzd09QG3pmgdSTpa1YxGOe7u141tY+3427aPatd8PZPma8fcbU6SEBiW9C3V+BOO32wvRvkSM9GxK5zydNm0vhU0tBFPX0G7o5NrPKaAsAqOfUDwB9GpxmFiw1g9SFyt2EEKIIYQwFvwf0UBEEZW/axeuP/DKyXFrgklQTRonFfy9IQVaEOVTnhMNlzdIBusIHcpO7lqE8udOtIyDeMKwJ03Jwt/unloESzumQtYez0AI1fXXyt/WJiiqhUhgSJHA1drrC3LPvboNnnRDOweD5rCGCSCrgFIA/QTWAcatbugHCZxK0cz56n2caB8iMbgiiohR+J5t+wPaiaxeeOXRjajr/pKkfu5M4++NbtYOGd3q8gbwQU1iCXE1qPTpMfkLSpbpctqavFSf67BELl61JxBLfF9tjaNVQt6eprCp67CVv2nQUlTjSSCeu1YRwUYjZcBlhKNzFI+leKaCVTV9ClNADWDtttaUg+g3EYwBJ8wnFVFojvdDRQQrNAnM5KomsZ+NyjZtSTDZwfZMVcCk1uVROrOIm1JOiJswu9pnbtnsq19PXh6WK6NDVrytptI1DzRmIX8V2uc6kGISnvEFMe1Yu1PSv4jakGpNtCKBAfFPNBDjjfFAtM+3IjTSs6nDqPnXL//196bKal2kgJFhMAWUGCE5SQ+W0QIxPhHBsETKUe9GtC/ZL2oRJKzX2qXIYKMmgowIOpuGJPJXIamjf02Uv7jUU/6I2/nc/R81XP6mFRZL/pybJbeiUnKKZ9x4fp0Yk8mL52W8/z0ZP9dl1lvLdhF7qoJO0fY3WRXBUo65LZqwpZM5sEf5fUkmgTHRQByPvNiHtF+bnzzr4v59ZszZdG9nCyqA9nNTUQCdxkFJ82qZh0Xw6kE1kRykQvm7RkUCd2knzO3crRxJc6JobsxkJ5nAt2vtG8iNcJ8nrgYpn9/Y+qhx4pebL/kLb5H8m6pS/l7uzEr1VrB4hYx1vyVj7xleRynbCfIjKX7ekKxISxoSqApkBtHAlBKoiWCzIoEt2jHd7Rdmw9r85CClT98c1mYBJAbCFFADWLutFR+crBo2u1wEdUtfIrQ1gpgQ1/Nj6ij5S1i0Jc2G70z9jA/2c/b9I67mpR/tNmzdHyJ9RdUflGmF07P6+8mhizLa0a7eG0SodM0DtZn8QRrp8IZUQZ5yDD6QpqxhvfSudB4XzePfDI/uu3lefrC02DXdw3CeQY2GkJ/TO9MSt55Nhpx/+nuH5FBbl6nbtK6hvdbIB/RzCigF0DgJ1DWQbhHB3KJCySsulsKKsv7coqLa/ZurTT2wKiIIucZVTabGOVv+og3fk20n9Ptr4FDGxbA1GITYgZHr/hDJK6xapUb29DLaccSotNB+RQBnZihkaK+QLDWzSk/0L8Fz4jiyL81zJiQprQjkQxsDOBcfWFyZL+9bXCC4dxL5BbntOTnTQqMj48/6pHqnkQIYlCyDGBYLYIsigBuNfECuASRGoKu1QWwTeSfJYFT48kumq/fTcq9e/dtotvwBRTpwIF+tiGC9ZLbYnThL/hAtbuJQxqWe8kfczL13rjRM/iKRv7sMe20QSTzm5ZOv632obM49OG4iCvV4nONjs9HyB/CYaPuQxjEZYOLfofw+IoG7k72en+wLhxQJDJ08PRZUblKQP02VwEXz86Vydp76fwsJa3OuIxKJ8FH49M9f3cARbirjYATQINZua4WcbDHltSr/8kqKZfySuZXOIHvqLT9ffb684oSpN02K/DVavc20iqFeWI/gJhqSrflLU/7UfYZr/xLC6B9xLej39/KP/m9ZPH+eMfJ36z2GRP6mMn7uXTUlVA+lax7IeuKgRebqJbImEF+vTtTywQgyODbHoq6Tg1TFe22KACZM868sKJBFMwqkoiJHps+YJjNvNmaONXzhSv/08mk4B3VqotLuszYNljDSs0m3DHScOK/czpn5MpvqGtoNnUcwBZQCaIQA4sBu2hqeimVLJUcRs8mxMeU2flUGx0dG5crkpPr15OUx9ec3vNfcHEXsiq6dZPPzVMmLfh//x2OnSUiRv1o7tx3XB5rP5Phlee+1X0h4/xPTkkwwMBnYl4a8oPDLao5qXEw9bhBiNkamfk6/7b64VT6NYuzUW3K5+y09D7FakUDd0oZjp5nyp1MCrzvfa/cHo984nnvxkcsyGZh7JTKn6Dk3LBcTFP/IKxQpmxs5heA+v/D600legcji1SnXFG5VhG8XP2mmC6DuC5EUQHfBFFDjMPVgDtErUCQtR7slic6ZzVa7B1prLdGgiGATRdB4Lg+cV+VvfGQwlGRSkW6lVrVhPEc1IY9wCIhbQcEXo+SvYOEtpsofyF9wi0yODutZE2hI5okV8qc9T38G6aDxCE65l2UT12+jebOK5MLomHQPDsl5ZZ5y3bxF+W/fu5EJdvR+KhDDFNFCZPxQAM0nLMxE8RU5HAJjeGXHelMP6BNTDqw20WTFur9MRFBbm4Ya4c3cC/XT33FYuttaIH/478Gp4qfcGiWSsphuy4KtVk12XEiN+KPZMvEo3/jyFwx5HLXPnyJnVoA2EWaLppOABGoZGKZJVHlhvqyYXS73zJ8rS8tLZXZRYdp/+/arE6l+JdC6p4bHSRKVVEIBdCQhsx54fGjI7vfWLw69CkcR1M9IX48qfn3vHLphf1akb4NyQ5pinyZ+6V4Fb0jVa8rnPM4hIG4FDd/vvWOlMVJmkfypspmbL4VVWddrc62IKMdiZO9sNHMSnZczTRaWFqsyeO/CeXLHvFmqEC6ZUaJIYoF6mzKnaO5798rGNM7bzJQwn4O65xHm9wGkABr5eeUQuGPnnLhse4PNrfs3Vzt64XVMaihOdFvk2mJ7kujCwsigKn2DPcfV/8/OmZRZuZNyS96Y1E0f3i7ra7MtDU35Sw4kup7DQNwICr985dHNxghZYbHkzbnZ0tePCCBSTnWuB3SjBLY8s742JBYVUyvJz1NvYHHZVelTewfjtUR/7+NSgyyRDUleT33rnpqm9Q3tFAAHw0bwFEA/Y1qJ2njFXawUW0X+XDOZV0QQJ5lG3BQZ3KCJ4AbuntcoHO6TiuMHpPjdyC5bIJMyR0bVFJ4Yglk8NMZ+K+UvJZQ/4lq++JlPGVL1Uz32WBj9iwUpp+N9p41sFO8WCVTPj1rrh3rt/Ghmn10IJ6JLLYmWA0DsFMHbLcmXFtRr53VCCAXQcZi+DjA3g9x6A3Ft/zZFBnGVsUVrIQEJ/JSfZbD44imp7HhR5nb95oafLS4vNWL/b+Cav7RgShNxJYj+GVX4BemYmUb/xoYuyanftsnZY6/L0LkzEZkrLpG5y2+TBXeukeI56YtpweLbZOTNlzN5+nUeE0FI4C6tRcUG7f0FJcvIYP+0y9Kn3PqnjUp/zmU5M22k6Sf7wmlJmyKBjYoEJsvaeVz5+S62gHDn/JVQAL1O2MwHvzI5Yct7clP0L4kIqusNcJsig1mf7NwCon0zT/9OlT4IYDxuKi5S125kCcZ2N/v8pU2NmHvFnRDTQPQPEmjIBCRD+Tvx8+fljZ/+RJXAqUAKj/xojyy5t1ZWfPqhtEQwt2y25M6slIm+077eploD+F3aLdqzMPaWUBr6FNl7Ke/MnsFp4/HOo48/tDGwS5HAdKUNa/kTLTuIVp/mecYc3CDWlFQDYR9Ag1m7rdW0AZ0+d45ym231UNnS9N1KFCEMaiIYvfrpGembefp1mXH+7aS/i0X6WcqfKn6YNGhXk0l67NQmMoS4CojfGy3/bJgAZtL37zffe0I6X0xvSTIigqs+16DKYCqujA7L0GsvpD0BLV3zAHuaTkGRvHpJ3M8UAph2+6jWPTXJjo84z1QxCmg8Iz2bgknkOy1+9cJxGR+bNO011jW0Gz5xZx9AYiQhsyTiyoQtEUDP9995eUddSGIquCpCGC3Pv0RcWqq/5oWvp57MFRbILTPLpCg3N9OHD2vi10zxywquRyWu5IF1aw2TPxR/MUP+ACKE+BuQSgKnFU6XvDmL0u0NyMh9HBTBa1YkcFUCcdui/Gy38jvhNB+uSTtGBuL8jFFAB2Om/BEKoBswbUI8MWp5L8Bmp1f+NEkIkWZwXaqBIoUB7YQUlcHoWhDHyWGyiB/KdKNHEyJ+0epsadKuSfKTXOOnz82FlWmJSzGq8idA+mU6HNv3k4zkb6o4piOB+TdV6WkOTyISuFURvUQXTBEdrE3ncRDda91TkywVlGsBCaEAOhKUVfTKFf4nuTmvSmFYIpGvULyfxwiiZCKGOfl55bkFBYGxS0NH4lxIiIpWP6RUe46OTF87In2liuyhWW+aDXqjz40bqre1a2tEiH5Y/IW4knvvXGlY5U918lFxU+oDUWdY3vjp07qeBxKIlFAUiEl4HC6eoQrpxMD5lI832PZcoHTNAzwexmejJm5TI6VBRQ43KJLYkqYEhtD2QeJXBWUUkBAKoCMx7aqUIglWvg8Ufwlxc2YsiFFCZjyHIoGpf3H6jNCSGSUHC3Nz1eIu8dg/PP3qiXXoyjR5dyJyKDg+lld7+uVnuN3Ng+mfxJV8bv1HDX28nOLylL/z2o//X0OeCxL4sf/2raSFYZAGmo4ASuRCHwUwDij2oogeIn2H5cZMhz3Kz0LpFoTRqoImWpePKGAz+wI6Bwt6AHJeQgF0PF5Jj9vNTelOLhbPPbj1V22NiX5eec+DuDob78pqmPJnKkz/JK4E6/4+e79xAoj1f1h7lwy0ecDNCKJrAu/7yteSCODNcvnk63JlIuVEtoJ7REoJjEYCK6aMG847WzN4uI0JZBKPtVP7OfGHABKDyeEQGI6peenoBWgRLdyUriWc4ufBBN9v4tCZCqN/xJWg+IuhE480ir+g5YORQCZTrSVMsy0FC8GklkBcCK+Ncy5CQZi0j4PaOr+NCeZVG1r31AQ52oRQAB3BKzvWmxoBtKgXYPv+zdVhbk3PCmC8ZsaI/jVz6EzlUxwC4kbuN1gAc1MIIBq8o6+f0STqIXhNABdxYxsrgWiZMXVOhFTQtKOoigS2S+JI3x6ONCEUQF8wOWFJmV0Wf3E3qS5CBLnNLQcTHkYOCAVQYVpB8r6jZshfVCxP/Lw18YRIEVOkp6ZgHfeItCUQkTtEAkNTjoUZiRuKwkikSfxUAq17aho50vYzbH4KaJijTAF0AyGzHtiiFFCmf7qYl3fUJUxDrrznwQ1y4xoWRP94EjWXIIeAUP40AUxj/Z9ps8hfpUgDTaM6KclMApUbJDB2icGGhzYGtmQogc0JJHC7IoG8uGYzI8PjZj9FJ0eZAkjMJcz0T1cTSvHzeFevufbPfBg1IK4E7R8Mn3jYFAEEiAImWwuYRn/CIPeKrESwUSLRwOgFyp2KBGY0lkkkkKmghFAAHYFp6wAnx0wPszP65+19b+oC/BDX/lkCJ43EnQJ4xwcMf8xkEUD0/jObZAKYMyN1g/rBtudYCTQ7CQwpd1XKLXrO2adIYCALCYwVSVDTuqdmJ0dYF4yiUgCJAVxwsQAe5OZzNQnTJLT2D1NPtls5ZKbD9X/Etdx+y1JrT54nO0x/DqSYIhIYV05z89OJAvLznL0EIiW0QZO4dk0CMxJqbU3g1CqjWxQJZKVlfeeprOnvNb1PdZibiAJITGT/5mpGAN1Nsgjg41P+33T65WfaOWSmE+QQEDdiRvonBCsZQ+fOWvLekqWZptGmIsC9Q7cIhrS1geg5nHH0TqsOiiqjsXOWPYoEctt4EwogBdD1k3BdjI+MmPm6Q9x0zuWebftTXnV+eUddsm0Ye3W0nYVfLIPRAuJKbl9WZfykI4Vc9Xd2WPLekhWaSSMCSMkwTgSbtYhgxqBPoHJDiwhksiAlFFGsfYoEMkU3c8o5BBRAoh/TmsFfMbcNBNM/nU2qk1rCCw+V9zxYH/P30ea6xBpYAIa4ksULrK+ImaxPn5EkjwCW8zPtIhQJ3CXXooG44Mb1gJmj60Jln/kpoIQCSEwkxCHw7PZ7JObrhtMvPxPmcLnjxEqIXdx+S5Wn31+iKGCqNhXCCKATJTCsRQORVsqiMB6jLrLuk1AAHY+p66rM6gW4f3M1P2DOJpji53EjuJX3PBiI+dutivxxnad1YOyZjkRcyZL53u6Jd+7NrNNAA6wE6lgRDCk3RAMPMhXU0PlFQsbHJzl6FEACXtmxvt/Mx78yOeE6aSWWkEjgt2v3zYr87eIwWS6AhLiSxfPnWf6cZjaBn0qy9YbTCotT/Tkj+84WwRasEeRImM/gxREOAgWQeFAeiHNYlUzgX95Rd8PJTov+1Wvy18AhtJwgh4CQa0wOXUz68/ziEsteS6JWEOrkKHUaKD/bxBOM9Gxy+r7M+SkF0FWYduVp4rIpvQCPcJM5nmTpLM8m+D7kbxflzzaWcAiIGykvM0fErkwkP39VLAlYd5JO0nR+WkHKCOAq7iXEB3OLlAwMjHIEKYAkBtNSKifHxl31eolhBJP8LNG6vrAif2z2bh8BDgFxI1Y3gHca0xgBJP5BVzrz+BjXAFIAiWvZv7maAuhg7tm2P5lIhF/eURd3+yny18zRc6y0E+JLUkUBrUTHmsOKwbbnuA6QeAFdmSrj4xNmvz62KKMAEjA5ZvjJk/LnfJIJIKt6EkLccw5Lsg6weM48R7zGnNQpoCDIrUk8gK4LGYMXmQJKASSxmLYG0AQBDHNzOZ5kE40nOTyu22aEkDiUzHWGAKaRAgrYEJ74XgDHzI8AsporBdBVHOFrJQaSqOBAwvRPQgjJlpOn3jPtsScHzif8WfGcuW4apg3cU4ibGenZpDuN2YIIIOc4FEACTKgCGuaoOp5ggu/v5tC4bpsR4ng6e86Y9thXxhOfw8oXV7lqnAbbnqMEEjejrwAMm8BTAIl1MAXUX2gFYBKVaW7mCBFCXHUOS7IG0Mo2EAbxKW5R4mJ0pTFb0QS+rqE9xM1EASTmwPC6swkmkr94zd+JY2CfMOJqLgxcslwAwdzlt7lpmDYMtj1Xwb2FeGx+kRZjjABSAMkNhM18cCOjgPs3V1MinE2iK3RNHBpHw0khcTWvHX/HlMdFG4gro8MJf+6yNFB8zpkGSlzHSM8m7LsBPY/B9X8UQOJeAeSHy/kE43yv5eUddWEODSHELE6eMm8d4ESSQjAL7lxjnb0Zk3L6CPcW4pG5RWYSOWx6T08GKCiAhB8u/3HPtv1YoB1vhsLiL86HTaKJqzGzEMzk0IWEP0MKaH5xiSXvMdHzZNisPjjY9lyAewxxGbrXr1oggGFuJgogicHASqAUQGcTjPM9rP0LcWgcD1NAiat58dBR885hSSKAwIooYLK1hqnWKcZhO/cY4oH5RUYMDJheBKaTm4kCSGJPTmPjRj0UewA6m3ipRVz7RwgxHVN7ASqClWwd4JJ7a01/f8VzDG06X88oIHELIz2bsK/q3l/Hx0wvAhPm1qIAug2urSO60No/TE0jbOLaP0KIFSAF1KxKoCBZFBDROYMFLe5zJBPULGAUkLgF3YWL+nuHrHidnO9QAN3FKzvWm5paOTFiWNidKaDuOUDjQLiLw+IKAhwC4gXMqgQKxvtPJ/35sk+st00AZSKrZRaIAnLtL3EDugsXDZu//o8CSAEkU7kyaVjYnZFK9xygG9j3jwJIiJW8+NvfmfbYE32nkxZbQRqoWcVgEF1MFmGcyC4CCHZyryFORkv/1H2hYmR43PTXWtfQTgGkAJJYJicmOAgeRqv+GXuAbmLhF0KI5QJoYiGYiAQmXmcI+Vv2iftNed7AfcnXGF4ZzTq9DRVBt3DPIQ7GkL6VFqSAMkBBASQ3nDRHRjkI3iY2+teuyF8jh4QQYjWvvfWOqY+fKg10+caHTFkLuOTeYNKfT2YfAQTbWRCGuGR+kTXD7AFIASQJ4dULkjH3bNuP9gH1MQfAWo4KIcQOUATGTAlU00CTVAMFd/3plwyWv9rk6Z8pWlSkAY7h+7j3EKdhVPrn+PikFT0AD3KLUQDdismFYBgF9CgbtAmEKn9c90cIsZMXD/3O1McfP9+V9Oco1lL9B8algq749ENJfz6pXwBBzWDbc3u49xCH8bgRDzJ4ccSK1xrm5qIAkjhcmTRkHSCjlM5je4z8cfsQQmzl+YOvmPr4Y6c7khaDAas+1yAVSwK6nwsimSqldOLieaPeWj3XAxKHYcj6v4EBSwIQFEATyeMQuJeJy2OSV6zvMfZvrmZ0yUHcs21/NPpH+SOEGMrcuXOvfl1RUS75+QXq1/n5+er/E/2u2UD+UAwmb87NSX/vvq98TX719a9Kf2d280IIZKron/paBs4b+fZ2KhLYX7rmgWbugcRORno21YtBFaoHL1oigJwDUQBdi6lyNTk2zhH2Ho9Q/ggh2YhdVOpiha6iokL9v14OHT8pdyxbbNp7uHzqrZQCiKqg2Uog/vbOR/88ZVuJZFVJdbBHkcAKRQLZx5XYPb8whIEB01NA++sa2hmgoAC6liNiULg9HlfYCsJT3LNtf0Ai7R4of4SQq0QlLip6c+fOuU78rMBsAUTbhTFFAvMX3JKWBP7me0/Iqd+2pfXYSPm8Z8vfpJVCmqoqqQ4QCVylSGAD92hiNSM9m1D4JWjU41kQAeQ8iAJIEjExyiIwXkIRvzBHgRB/EonaVaiRu2JFcnBfUlKifF3siNcHATQbrAXMu6lKpuXmp5RACB0E8MiP9sjQuTMJfxdr/pD2mU5DeVQjRVVSE8GaQEzEaxURZHSDWMnjRj2QBf3/KIAUQJIMI5rB1+09Edi/uZriQQghFoHIXazoGZWmaSZDo5fNjwJOjMlY91tSsPi2tH5/wZ1r1BvSQXsOtSn3HTI2dEmN+CHah59l0kMwVTVSg4AAdigiCAnkJJeYjtb6od6ox7OoAMwRbjkKIEmAQW0gcGCgABJCiMFEo3rXhK9Y/b8bOXv2rPzyN6+ZKoBg7L0OyZ1ZKblls9P+G8ie3gqhqnye7jB9HMcVke7tPl1x8Wzv4dP/+sOGyk98vpmfFGIy2418MIsigJyXUgBdTcjoD96NJ61JmZbLbh6EOAxe2fchEdmbo96Xl5c7TvYgcde+PndtQtffL2NjYwn/f3WnPvRb+as/vt/01znacUSm33ZvylRQQ8XsvdStKPTS2f6GnHj1sIwpEgjOvNO5R5FAoQQSszA6+gcGLKgAWtfQHuLWowCSJEyMjkieQ9aIEEKuzaE5BN4Hkb3IbY6lBVmmMjQ0JJcuXVKlrb//wnWyNzR0SfmZMVfsLwxckh8//4J89v6Pmvp+UBDm8sk3pLBqlSXjZ0X0781fvSphRQBjuXi2V177+UFKIDETQ4MQI8Nj6s1keAGVAkhSCqABvQAJIYSkZsGCBVeFz+roHoQuKnhRqTNS7tLlR63mCyAYP9elpoGmag1hBFh3aGb078w7J2+Qv1gJPHbwVVQIDZWueSDMTxkxTNYilT/rjXxMNoCnABKH7MQG9AKs4GYihJA4B0dF8iLSZ02ELxrJQ3rm2NhlVfYSpWPaxYu/PSone87I4vnzTH+u0Y52mVY4PaP1gJmCpu9Yd2gmSPtMxvmuUxWn3nx7p/LlRn7qiIHsNPoBLVr/xwIwFEB388qO9eG121pNFkDdEwNcIWrh1iKE+B0UbVm4cMHVSJ+ZlTkR0YtG83Afuz7P6Xz9+3vlu1/dYslzjR7/jRTdeo/kFM8w/LER9cPjmwmKviDKl4r3ToQ3DLY9F2AUkBjBSM8m9KAOGv24fdYIYIhbkAJIzBdAQoh5J7Egh8HZRAu3LFmyxLS0TsgdonqI5iHKh3s389zBV+QbA5ekvKzE9OeCpI28+bLhEhh9XLMLv1w815vW7733jtpnMSBMfyP65Q8HMsOjf+Pjk1Y0gAdcA0gBJCk/kCMjeh+inKNICPGb9EH4EO0zutE65O7ChQtXI3xul714oBjMPz31L/KVR//YkueDpA2//isprKoxZE1gVP4mhy46bWiDwugH0c927WKCoVgU/Wuva2hnETUKoCcIiYlRALSB0NkKooabiBBC6cuO2OhetFCLH/inp56VL37mDy2JAkbBmkCs2StYvCLrFhGQPjyOVfI3Y84sfviIZWiFX0zJz7Zo/R+jfxRAki5sBUGII8GJLMhh8Jb0RYUvcn/Wt2NrdRQwCqqDTvSdViTwtoyjgWOn3lLbPZid9nndJKuwQG5aujia4kmI2ewx64H7WACGAkgcJoD6WkFwgkqISXNkDoG93HXXnbrX9WHNXnf3qavCN8Z11yolJcXykxdeki0PPyjFiuRYiVq8paNdLitCl69IYN7sRWq10Li/Ozos4+e7ZOzcu2p/QTuovnt1ugLI1DeSNSM9mxrFpKwu9P6zaP1fiFuSAugVDpotWXpbQdTtPVGxf3M1TzyEGAs/UzZz6lRPVgJ46lRE+HBvdZ89p0lecXGJMoblkp9foBbLQWXU2DHd+0KbfKHuI7a8PrVhfPdb6g0poVOLxExeHrZN+mIpmztLVn78Xjn6/72Y6leZ/kaylT+I33azHt+i6J/UNbTzM0ABJOkyPoQPpq4+SThwhDiShBgKT2S2C+ApWbFiecrfQ1QPv4tIH+79KnpofRH5ujjtvof/+3cn5D/etUIWz7N3rRuiglgf6FQWLq+W6TNK1Z6Ave+evu5n+YUFsqTmNn5giR72mPng/b3DVrwHzkMpgJ7C9CgAUkB1EuBmIoR47uCrtV2It/4vmtrZ2dnpyUqdiYDYIaIXjewZ0eB+7y/b5G8/8wnucCmYtbBS1nz6kzJ8cVCGBwav+z4h2TLSswktH0wt6Hf2zIAVb+UgtyYF0EuYHgUwoBcgBZAQ4wlxCOwHkrdsWbUvpS8qe0jZLC8vN63P4ZsnT8u//eYNNRJIUoNIIG7xrllwdEiG8hcUk6p+RhkcGJXxsUmeMymAxIkgDVRHJdB1HEFCTAETugoOg31A9goK8j2f3onUTQhfeXmksb1ZspeIll+3yx3LFsuc8lLudFlSuuYBpo2TTOQPH/J9Zj9PT7dl9cy4/1MAPYUlO/T4yKgeAQxwMxFi2uc/yGGw0cD7++Xf//03nntfkL1ohA/3KM5iNdGqqGh4PzZ2WR47+Y78r29v405HiDVA/ky/0sMG8BRAkgWv7Fjfv3Zbq+nPM6lvHWCAlUAJoQAS5wsfontGrNvLRKCROgvJGxq6pFZFxffitcM4fvyE2hsQDeJJxoQ4BCRdtJYPpp9b2P6BAkj0ERaTo2wTo7o/oKwESojxdHIIiBuEL1b0rkX2Mr8m+Df//fty7x0fkNtvWcqNmOEm4BCQNOUP4rfdiuc6e2bQqrfFAjAUQApgNozp71UVpAASYjhc00DSAmv4FixYcFX8zErpjIodRO/Chci90QVxPvlnX5E3Wv5ZystKuGHT5wiHgKQhf5hL7rPq+Sxc/8f5JwXQk1hyZW9iZFRyiwqz/XMWgiGEJzViIVHhW7hwQdxWFUaAaN7Zs+dUyYPwWdHY/sLAJVUCf/adr1MC0yfMISAp5C9a9MWSCk8Wpn9y/R8F0LPgyt4Gs59kfGREjwAGuZkIMefkJib3aCLuIFqpE+KHm9FEJC+SwmlGZC8TXnvrHfmbnd+X7351Czd8+scJQpJher+/WCxM/3yWm5YC6FUsiwDqoW7viZr9m6t5EiKEAkgMlD7I3pIlSwxvzRAb3Yuu23MSP3r+BfWeEpgatoAgydCKvtRb+ZxM/6QAEmMmgOYLoP5CMBuEVyEJMZqDVp+4ib1A9CB8Rvfjiwpf5P6sK8bCjxJ45p2TEm5/XaaXlUr13asTNX3nBJikK384f2y39DmtS//sr2to5/5PAfQslkQADSgEw3WAhBgPT24+AJG+JUsCEggsMWw9HyJ7p071uEr4/C6BwxcH5ZD2fqMyuObTn5SyubOS/RkvvJJE8ofskT1WP29P90WeHymARC+v7FjfbkUvQKCzEEyQ/QAJMZywWFAJmNgjfUamd6INA0Svu/uUI1M6KYFpCODA9eumxkYvS9tPfyYrP36vzFu6ONGfsQIoSSR/B+x4bgvTP9n+gQLoi0mg6RPAMWUCoUMAAdJAm7m5CDGUkDAN1BOgPQOqdkZSPPX354PonTp16upaPi8DCewfuCT/Q5FAr1YHRdpnfmGBKn6xEoio4KybKyVQc1s8EQzxk0WmyF9Ak78Kq5+7v3dITQG1iBZubQogBdAA9BaCUfgUBZAQw+E6QJcD2UN6JyJ+enr0IaoXEb5IpM9LUb50eP7gK2qLiKf+4e9k8fx53hPAGaVqyieifrESCHrfPa3eIIizFlZK2dzZUl45J1z1n/4szE8YiZE/S9s9TMXC9M9wXUM7930KoOdBjn/Q7CcxqCE8IcRYcJVzD4fBXUD0IH3Lli3Tta4vKn0QPtz7HbSIuOdzf6FK4L13rPTc+8N6P0jgodYX1DWBN+wPihi+985J9Xbbf/hQiJ80MkX+EPmzpXL0+PiklemfjP5RAH2BJZ+oSWWigVtO9leoK+r2nqjfv7m6mZuMEMNAbh/bQbiEaLQPaZ7ZgvV8EL7Ozk7Pp3ZmdUJEs/jHviJfeXSzcvtjT0rgh//4U3Li1cMSbn8j/gWGwgJZ9IH3swcacYT8AQvlD3DfpwD6gpBYVMZ3fGRUCnSkKAnTQAkxgycpgM7FiGhfNNJ3/PgJSl+afP37e+XFQ0fVdYFeSwnNUwTv1vvuliU1t6kiiIqgsWmhSAMVrv8jDpE/0BXus+qp2P6BAugbLJsNjF8akoKyUj0PsYHVQAkxHJ7sHAgqea5YsSLrtX1M79TPi789qqaEIhr4xc/8oefeH9YFogoogARePNsrvd09Mnfp4vbSNQ/wPEv5c4T8nT0zyOIvPmLalStX/PnGp02z/DnXbmu1ZLBRBbR8aUDvw2xVBHAXPyKEGEqHsB2EI0Ca54oVy7Ou5IkiLkjv9GMhFzO5/Zal8o0vf8GTawPjnWcVAeR5lvJnu/yBw21d0tc7ZNXTbaxraLddAv3qQIARQGuxZA0QKoFemZiUabk5eh7mceXGExMhxoI00O0cBvtAmmd1dXVWffuwri8c7lTELyyXLg1xME0ABWKwNvBz939UjQh6sVJoDIyCUP4cIX+I/Fkof/1OkD+/k8MhsJSwVU+EfoB650l1e09s4CYjxFCaOQT2iV9d3Sflrrvuylj+EOl76aWXZf/+n8kbb7xB+bMA9Axc8an/LI99bZec7DnjxbeI9M8wtzTlzwmvp+PEeSufjvJHAfQdRywTwIFBIx7mcW4yQgwFE752DoO1LFtWrYpfJsVdEO17441j8uyz/yL//u+/4fo+iqDRPMmt61v5g/R1OEX+EP1j9U8KIDEXyyZ+Y8ZcoQ7W7T0R4GYjxFB2cwisJRN5w9q+2Ggf1/c5SwQ/89f/TW0m7wEYBfGv/CHyV+GU19TV2Wfl0zH90yFwDaBHBdCAfoBRsF6pgZuOEEMnfjudNAHwOkjZRFuGRKmf0UqeTO90PpA/3JbMnyefvf9j6lpBF64TZPqnP+Wv3mnHfosbv0fPf8QBsAqoxVhVCRSULKiUwopyIx6qav/map6sCDGOPcqtnsNgHUgDXbVq1XXfixZ1OX78OCN9LgaVQz+riOAD69a6RQZZ/dN/8rdFkz9HgbV/HSfOWfmUq+sa2h2zDMLPVUApgNYLIEL/QSueC70ASxctNOKhmhUBZBSQEONAGtBhDoN1oN/fJz/5yavih2gf5I94TwbvV0Tw/nV3q187lJns/+cr+XPkBT9E/146+LaMj01a9ZRhRf6qnDQGFEAKoJUCiCtAWyx5j7k5MvP9y4x6uNWKBLJ4BSHGYdnFIBIBEcALF/opfj6hvKxE7Sd4750rFRmsckpvwWZF/nhB1R/i56hKn1M5/uYZ6Qpbuv5vqyKAjop8sw8gsRLLKoGiF+D40JDkZVD5LgkQ11puPkIM40kKoMUH3yNHOAg+4sLApatrBqOoMrisSo0OLl4wzw4pZPVPf8gfpG+fcgs48vUNj1ktf6CZe4ZzYATQYtZua7U09ato1kwprjRsTcTG/ZuruYCXEOPocOoEgRC/gIIyixfcpIpheVmpIokfUL9/+7KlahTRQMKlax6o4oh7Xv7qJbLO27EcO3ra6uIvzXUN7Y6LfDMFlAJotQRaNui5RYVSvtSw+WVYIqmgXLtAiDE4fqJACIlEDqNERXEqSDNNJoz33rGyQRHAZo6mZ8UPKZ87xeEFvgYHRqXt12Grn7ZWEcAQBdA5MAXUHvAhCFrxRBMjo0a1gwAwSaxfbOQmJMQQmoUtIQhxPC/+9mjcrzP8rFP+vCt/yO7Cxbwap7/W48fOWP2U7U6UP7/DRvD2YGkxlcsDg0Y+3Pa6vSdquAkJMQw2hifE+3Dtn3flr14cXOwllrNnBqWv1/JepzzHUQCJhqWVCEb7Dc/zZsoaIcaBqmhMqybEu4S0G/GW+FUot33anMgVWRw2RP/66xram7m3UADJtZOBZUTTQA2kpm7viUZuRkKMOUEqtyYOAyGehZ9v78lfUCIF/Ta45TWj6Tuqf1oMo38UQBLllR3rw2LxFX+D00ABU0EJMQ5EAcMcBkI8R0gY/fOS+CHqh3XbSPkMuOZ1o+1DZ6/VT9uvndsIBZBMOSlYhglpoICpoIQYB6MEhPBzTZwrf0GJRP22uO21o+3D+Nik1U+L1g9c3kABJFM4aOWTmZAGCpgKSoiBJ0thpIAQLxHiZ9oT4ufKqF8Umwq/AKZ/UgBJHNqtfkIT0kABUkGD3JyEGAKjBYTw80ycI39Y4+fKqB8YH5+UY0d77HhqRP/C3IMogGQKr+xYH7L8QHa+z6yH3qNIIPuYEaIfHBeaOQyEeOKzHOIwuFb8AlqFT9wCbn0fkD8bUj8BL35QAEmKE4RlIAUUqaAmgIMj1wMSYgxbhW0hCHE7nAC7V/4axWUVPuOB1M+z7w3a8dSM/lEASQoOWv2EI72mRQE31O09sYWblBDdsC0EIe6mRRj9c6P4bVBuHcqX28Ulff0SYWPqJ85fW7k3UQBJciw/QVweGJArE6alA+xkawhCDAGls9s5DIS4Ek6A3SV+NcoNBV5cne4Zi42pn7tZ+ZMCSFJgxzpAyB8k0EQOcD0gIYbQwCEgxHUgeh/mMLhC/LDOD8tXkO4Z9Mr76urssyv1k33/KIAkAyyXQBPTQAHk7wA3KyG6aRemghLiJsKcALtC/Cpi1vnVe+m9DQ6MSseJc3Y9fROjfxRAkj7PWv2EKAQzPmRqTxj0B2RRGEL00yhMBSXELbCAkzvEzxPr/KaCdX9v2Jf6GVbkjxc/KIAkA0J2POlo/0Wzn6JekcB6bl5CdNPASSUhrjiXt3AYKH52cfzYGRm8OGrX03PJgsuYduXKFX++8WnTHPNa1m5r7bPjgFSxbKnk5Oeb/TQb92+u5kmREH2gwu5ODgMhjgQXaFYL1/45Tvy0Y+fjXpW+KD3dF+TY0dN2PX2orqG91o3j5lcHAowAOgNbBMnExvCx7GFlUEJ0s0sYXSDEqeym/DlL/PwQ8YuCdX/H3zxj50tg9I8CSLLkoB1POnrhgpktIaKoRWEUCQxwMxOi+yTLSSYhzgJrdBs5DI4QP1T13OkX8QNY9/faoW671v2BJjZ9pwCS7LHlyj7kz+SKoLESuI/tIQjRBdLMNnIYCHHUZ5LRD/vFL6i1c4D4bfGD+EU51HZSRobH7Hp6iB8Lv1AASba8smM9TiK2VPob6e21IgoIkAbKHoGE6APHCTaZJsQZNAmr9NopfvVaA3fc6v32/rHmz8aiL6CBbR8ogEQ/z9rxpBZGASmBhBgDrrg2cxgIsZWQMPphh/QhzbNRuSHah6hf0I/jgGbvKPxiIy2K/IW4R1IAiQEfJtsOqNZFAaMSyGqGhOgDUUBGHgixB6ZjWy9+G5TbPrm2vi/g17GA+KHlg837P1OfXQ7bQDiItdtaO+w6qE2fO0e5zbbyKZv3b67mAYSQ7KnQJkOMqBNiLZA/VuU1X/owH6pXbo/4WfhiQcVPrPuzseiLuv/XNbR7Yv9nGwjiFEK2HWitjQICNIrfw01OSNbgKmytsEk8IVbClizmSl9FzNo+30f7HCh/LV6RP79DAXQWz9r1xBavBaQEEmIMSANlJJ0Q6z5vLMJkjvht0Cp5YiLi27V9iUC7BwfIH1M/PQRTQB3G2m2tOPjZktI1LTdHKqrfp95bTEi5bdy/uZqRDEKyo16bNBFCzJv8Vgkj7oZKn3L3KeW2QZjKnlL+bK74CWq9VviFKaDESdgWWkcUcOg9WxYWB4XVQQnRQ7NEStITQkya/FL+jJE+RPqUGy52o6hLPeXPFfK3i1U/vQUjgA5j7bbWDdpB0TYqli2VnPx8O54a6TW1jAQSkjV7xIf9sAgxGaS9NXMYshI+yF1QGOlzs/y1K/K32otj7OcIIAXQmRJoWxooyC8plrIli2w70OBkq0ggS9wTQgkkxG6aheueMpW+gCZ767R74l75U4uNKQLoyTkZBZAC6DQBRJ+8LXa+hhmBRZJXXGzrAYcSSAglkBC7KFmwtH3dt/4NRV+Cym2JXKtGGYzz62HtBg5q5zGcw9r9kNWireeLCl+Ae48n5A80KPLX7NWxpgBSAJ0mgGiWftjO14AUUKSC2ghOmFuVE2ezEEIogYRYwE13fVy9zV5+t0yfu9Coh4UIhjQxDHlBCBXhC2oivE5YsdOr8tesyJ+no98UQAqgEyUQAlhj52uwoTl8PCCBu3haIIQSSIg557qbpeoT9bJw3aclv3iGFU+JYm9o+9TiFhnUhK8mRvi4ls/b8ufZdX8UQAqg0wUQKaA77X4dNhaEiaVZE0EWhyGEEkiIYeK37MG/kJvv+7RdL6Ffk8HdTlryoBVuqRFG+CwDTd5fO9QtI8NjTng5assTRQA9P+eiAFIAnSiAOAD32f06bC4IEwtOjugVGOapghBKICFZn9eKZ0jgk/Wq/DmIkHJrUs5xIRuEr0auRfeiXxML5c8BTd5jqfVLywcKIAXQqRLoiElbceU8KZo10wlD0q9JYEgIIZRAQjJk9oq75fb/8k0j1/e5SgRjZG+VXIvyEbsmNb1D8trhbifJn6eLvlAAKYBuEUAcmA/YPla5OVJR/T713iHg5NjIUwchGVOviSAhvgJRP0T8EPlzCUgN3Zpt1ktMGmdU9gKUPWfR031Bjh097aSX5PmiLxRACqArBFCTQNuLwYCCslIpXeSoK6Y4OTZwXSDxO1pxBkkwuYuWou8vmv90OyWQ+JEZS5bLnV/+rpOjfonA57cpWSG0KaK3JOZrFmlxMMffPCNd4T4nvaSQIn+1ftsOFEAKoJMF0DGTNQelgkYJaxIY4umE+ET2AhLps7VKE75Ahg+hlqP/4dMdFx7d0vY4J4nE6yDq57C1fllNzjdV/bJpU+CFgPaZX6V9doPcwu4ClT6PHzujRv8cBM4LtX4o+kIBpAC6RgA1CexzwkQNKaDlSwNOqAo6FaaEEi9LH67mPyIGN1i+cHFMFBGUf/z+W9LZdYkDTTwFUj7v/MvvyKzld3vi/ZTkjcifLGuV2spD3LhuPZYPj6nr/RzS5iGKbyp+UgApgG4UQMjNdkecVJ1TFXQqrBJKvCZ+9codonSmp4A/96/dsuNbv5MjrzOjmrgfFHq548vfsaqnn6VAAP98+TPcyC7DgcVeovKHyF+7X7cLBZAC6HQBRPSvQxySruWQBvGJDmZNbBxPXCx9+Ixv0cTP8s87IoJ//dXD0n9xjBuDuBIUeVnx+W2efo9VpT3ytdU/UKOCxPl0dfapaZ8OZLWf5Y8CSAF0iwTu1CaGjmBGYJHkFRc7dbhCElkbGOaph1D8MgOpoYgGIjWUELeAaN/tj31Dbrrr4754v5DALy1/Rr0nzgTr/Y4d7ZGz7w068eX5qt0DBZAC6GYBDEgkCugIsA4Q6wEd1BpiKowGErfIH9b24QJPwEmv67XX++XRx19lWihxPKjyeftj31Tv/QQigIgEUgKdB5q7v3aoW133R/mjAFIAKYB6JdBRjZwd2BoiHiGJ9FLydZoDcaT4QfjwmQ46+XU+8f231Igg00KJE/Hyej9KoDtxcMon5Y8CSAF0qQBiwtjhpNfk4PWAU2lSbrvYN5A4RP6Q7onCTq5ow4AqoY9uaZNfvXSGG484hpvve1BN+/Q7lEBngJTPo4e6pa93iPJHAaQAUgANl0BHRQGBw9cDxhKWSDSwhYc9YpP4Qfj2iUv7dzEaSJwCUj5vvu/THAhKoCM4e2ZQXe/nsCqfsTQp8tfILUUBpAC6VwADyt1hcVDkAOsAZyxZLLlFhW4ZxpCwSAyxXv6Cmvy5uvk6o4HETpDqufzhbZS/OLA6qPU4tLH7VJoV+Wvg1qIAUgBdLICaBDaKQ/oCRoH8QQIdXBQmHigQ08S0UGKB/NVLZL2fZ2A0kNghf3f/nz/2XbGXTCXw2x98ggNhAejt98bR004t9BJlqyJ/LIZHAbyBHG5+V4IPs6OkZWJkVC6dcl3qCdZhddTtPbGFuxQxUf72eE3+wJcevUVe/cUfyH0fmseNTEwH0kf5S03H4Hz5x2MPciBMRI36vXlGDrV1OV3+Gih/JBGMALoUJ0YBQWFFuZQsqHTjkIYlEg1s5mGBGCR+SPVEe4d6r79XRgOJFfLn10qf2fDny5+R2spDHAiDccFav1j543wmBUwBpQC6VQJRETTgtNcFAYQIuhS0i0ChmBAPjUSn/B1QbjV+ec9cG0jMwO9tHvSAVFAWhTHomD48pojfaSdX+KT8UQAzgimg7marE1/UpVOnZbT/glvHFBP2A3V7T+AW5C5GKH/psWRRifzbM7Xyra+tlooZ+dwRiG7Q5uHubYz8ZcsTxx6US+NFHAiddJw4L20vhd0gf/2UP5IujAC6nLXbWjHRdJyouLAyaCJCEkkNDfFwQSh/6cFoIDFC/tjjTz/33/yS/MmyVg5ENjbljiIvsfJXq8hfO7dc+jACSNyMI0v7XpmYlIudJ9XiMC4Hch2NCG7g7kZSsM/v8gcYDSSUP2fw/Lsfktf7qzgQGQDhO9zW5YYiL5Q/kjWMAHoApxaEUcc5N0fKlwYkJ98zk8CwsFgMiTdpiFT7rOdIXA+jgSQT2ODdeOYV9cl37/kWByIFqO7ZceKcdIX73PSy2zX5YzurLGARGAqg2wUQaWdoDh9w4utzaY/AdETwSeW2i30EiSJ/jeLQizBOgZVCCeXPPjZV/VI2BV7gQCQA6/y6OnvdUN0zlpBy20j5owBSAH0qgJoEIj1xn1Nfn0clEODA2yKRqGCYh1Nfyp+jP3tOgtFAQvmzD0QBEQ0k1+jpvqDKn0tSPWNpVsSvgVuQAkgB9LkAahKISahj16l5WAKjhJTbbkUEW3hY9Y38BSQSfa/gaKTPc//aLY8+/iqjgYTyZyF3lh6Wv/vg/+JAuFv8ACt9UgApgBTA6wQQk9AOJ09GfSCBICyR9NBmRgU9L4CQvxqOROZcUOQPEvgvigwSf4L2DmjwjkbvxHwGu7rlmx/9qdQsPE3xc6f4IeMIKZ8h7s0UQAogBXCqBDo+Hc0nEhgF0cAnGRX0pPw1Ctf96YbRQMofsYa+3x+XVZU9smvDzyl+7gPFXhpY6ZMCSAGkACaTQEengvpQAgGu3DVrMsgDuPvlD1G/wxwJY0A08K++elh++HQHB4PyR0xgtP+CXDoVifzt2vBvvokCekD8QIsmfyz2QgGkAFIAkwqg41NBfSqBUSCASBFtYYqoawWQqZ8mgOIwKBKDYjGE8keMY6CzS8YuDalf1yx8z9NRQLRzgPihnYPLxQ9sVcRvF/dgCiAFkAKYrgS6ojIh5A8SCBn0KaEYGeTVPXfI3xblbidHwhwQDUS7iH/8/lscDMofMUKIhobkYrjruu95MQoI2evpvujGdg7x4Ho/CiAFkAKYtQS6ojE1JfAqSPN4ljLoaPlzRXTdC7z2er+6NvDI6/woeAFIH+QPEkisJTb6F8VLUcD+3iFV/BD18wghYX8/CiAFkAKoQwAxST0gLkhVgwSWLJgvBWWlPCJFYJqoMwWwUVj4xVJ2fPt1eeJ7v2eRGMofyYJ40b8oP9j0vFTP6XXn+xqflLPvDUhXZ58MXhz10iZrUsSvkXsuBZACSAHUK4GuKlZRsqBSCivKeVS6UQZDwgIydssfo382wQbylD+SHfGif1E+cevb8rcf/bW7jsPDY6r0IdrngTTPWMISKfQS4l5LAaQAUgCNkkBXrVkqmjVTiivn8cgUH6SEIFX0oDBV1GoBbBRG/2yFLSMofyR9kkX/QGnhZXnq8z9V7x39PrRo3+nui9LXO+TFTcUqnxRACiAF0DQJdMV6wCiIAhbfNM+PFUIzJRodPMheg6YLIKJ/AY6EvbBIjDu4+b4HZfnDf0f5s5H+4+/I5FjyiyWIACIS6MjXr63tO3tmwGvRvqtvUSJVPpu5t1IAKYAUQLME0DXrAaP4uE2EHlQZxL0ihCEOh2HyV6/c7eFIOAcWiXG2/N3+2Dc4EHYes3r7ZOh06pTpj1R1yY66A8553VolT6R4eqCFQ6pzNaJ+Ye6tFEAKIAXQbAms0STQNWuYWCHUMCFs16SQs+XsBBAtVTZwJJzHE99/S40IMi2U8ke0Se3EpPSfeFu9T4fnv/CUrWmgEL2zZwZV6fNYQZd44BzcxN5+FEAKIAXQagl0RX/AqbA4jGG0azdVCllUJi35wwWTPo6Ec0Fa6F999bD88OkODoaNLHvwL9QbsRdE/hABTBc70kB9Jn1RQsKoHwWQAkgBtFECG8WFxSwggBBBYspJCSJ4hFIYVwBdedHEj6BK6F8rIsi0UOu5/bFvys33fZoDYTOpCr/Ew6pqoD6VPsCoHwWQAkgBdIwEuqooTBSkgpYtWig5+fk8clkjhZ2aFIZ8LICu/Kz4GUQCIYJMC6X8+Y0L74RlYiQzuaosG5SnHv6pKa9ncGBUFT5U7/SZ9MWeSxn1owBSACmAjhFA1xWFubrt2DTeLsLa7WD0az+IoSKAh934OfH9RJjVQk0HFT7R5gHtHogDjlVpFn6JBwQQIqiXaMuG/t5hL1fvTAdW+KQAUgApgI6WQExuA258/ewX6DgxRMTwgkSuePZ7JZVUEcAr3MTuBdVCsT6QTeQpf14G7R4Q/Uu38MtUUAkUFUGzMp3eIenThM+nUb6pNGvyx1x0CiAFkALoWAl0XWXQWJgS6ho5xK0z9v+KIIad/uJPHq6rmVdZdpib0f2giTxEsLPrEgdDJ2zw7jwGOrtk7FL2TdLr1xyR+g8eSet3kdaJlM6I+A35Oco3lXZN/EIcCgogBZAC6BYJdO0kFymhaBrPKqGupF87aYKDU6RRPaHa2bpi/56a4H0fW3YgL4+9KL3Cjm+/Lk987/dcH5gls1fcLXd8+TuUPwcx2n9BLp06resxkhWCofCldR5jkRcKIAWQAuhKCawXlze6xppArA1k43jPEor5+mDM17HCqP7fqOiiIoBblq+s3Dl/IS8ueAmuD8wO9vhz4AQ2w55/iahZ+J7s2vBzdQ3f4MURNaUzKnwkKc3CdE8KIAWQAkgJtHm7skAMSS2PkkAkb+ATY99ed2vuq8EPrXufMAroPZAO+uiWNq4PTIMVn98mgU/WcyAcxmBXt1we0F+8pbqsU/60+kmu4cvsnNLEdE8KIAWQAugVCWwUF/YInAqjgcQIPjb+T3LrxAFBBHD5Svag9CoQQKSGUgRvBKmeiPrddNfHORgOQ0/Vz6kEpnfIwwt+wEFNTVgTv2YOBQXQzXB2TK7jlR3rIYCuP7DhiijSYoy4Mkr8S9mVyOQKfaxwI97kvg/Nk397pla+v2uNLFlUwgHRmD73ZrXYC+XPeaDq5/DZc8ZZzXAVBzU56jo/5baa8kcogMSrEtjgBQnEmgikx+Cmd30EIcffPKMWQyDe5fObquT3bferIlgxw9+VhVHs5SP/17+wzYNDQdEXI89rRTkjHNTEoLhLlSJ+jVzrR7wCU0BJQtZua8V6wHpPbO/cHJk+d47aO5CQdHl09BEplGttA/Lyc+SONYultKyQg+NxUCgGRWL8WDEUa/2w5o84k+Gz5w2N/qnbnCmg8WiWSLpnmEPhTbgGkAJIfCCBIL+kWG0Zgf6BhKTiS6N/dMP3iqbny5oPB1gUhiLoObDeb/nD2+Tm+z7NDe9QJkZG1Ybvhks/BTCWkHJroPhRAL0MZzAkKV5JB42CRrk4eWLhPNNCSTaMDI/JobaTarl04n3KZ+TLtr+8TX7/7w/Inz96i2ffZ7S5O+XPwZNV5Zw10NXNgTBX/GoV8aul/BGvwwggSQuvRQLVfYAN5EkK4kUAo5TOKFTTQRkJ9BdoHYGKoT98usMz7wn9/ZY//Hds7u5wsO4PTd/N4O7yl+QP5rT6WfzY0sGHMAWUAkh8KoEAaaHT586WvOJibmSStgACpIPefsdCrgmkCLrz2MeUT9cA8YMAmsW6Wb+UdTNfoPgRCiAFkAJI4kpgo3igT2A8EAmECObk53NDk7QEELAwDEXQjSKIlM/bH/smq3y6AKz7u9h50tRlC48s+IEsmd7hlyFtVm5PUvwIBZACSDKTwHrlbo9X31+0WiibyJN0BDAqgbevXigVsxhF9ituKhaDKp/LHvwLpny6YYKqSB/kDxJoJv+16u/90AoC4seqnoQCSAEklMAE+4cif0WzZlEEKYAZ/f7ylZUyfyHXlFIEnSmCEL47//I7Mmv53dxQLsHMdX8+EcB+Tfx2U/wIBZACSAE0RgKDyt0+5Vbh1feIdFCkhbJQDAUwXRYFZsqyW+dx8CiCalooZBBponZz010fl9sf+wajfi5ipLdPrVhtBZWFPWobCA9JIGTvSeW2i83bCQWQAkgBNF4Ca5S7A16WQIogBTBTZs4qlpV3LGSFUKICEcQ6QTtEEMIH8YMAEvdgVr+/ZED+IIGQQRfTLpFoXzP3IkIBpABSAM2VwIBEIoE1Xn+vFEH/UCiX5NHRR7L+e7SJWLFyPovDkKv86qUzqgji3grY3sGlk9KJSek/8bYtvWpdLIEQPhZ2IRRACiAF0GIJrNAkMOiH90sR9L78bby8XeZcCet6HBSHQToo1wWSWMyuHDp97s2y6rFvcK2fS0Hkz+yiLx6RQBygkebZzPV9hAJIAaQA2iuCnuwVmEoEC8rKWCyG8pcQrgskcSf6WsEYiKBR6aGo7okbcSdWFX1xuQSGJBLta+YeQyiAFEAKoHMkEAK4x1f7E6uGeoa6sW/K0sk2wx8XKaFoFYHm8YRMBRL4w5+Es04Pnb3ibrn9v3xTps9dyMF0KWY3e8+U8lkF8tjMRvWimANgNU9CAaQAUgBdIIG+KA4TTwQRDWRDeXfysfF/klsnDpj2+EgJXb5yvsydV8rBJnFBJPAJLSqYThsJpnt6AzuKvqTet+bIojkDakaEjRLYotyeZbSPUAApgBRA90hgQHxSHCYeBWWlUjR7puQVszm4G1g+EZKPjj9hyXMhJbSqeg6rhJKEID30X372riqDR16/sYo9Crsg1RNN3Ym7mRwbU+XPjqIvqQQQFzOREYHMCAuBCXNtH6EAUgApgC4XQV+tC5wK1wk6n4WTr8vGse2WPierhJJ0iY0KXhqfrkofbqzu6YEJqCJ9FztP2lr0JZUAgjUTP5E14z8x8+lwlQPRPlbyJBRACiAF0EMSCAHcKT5LCb1un1Pkr7C8XI0KMj3UOZTkjch/nvySTA7b0yt42fJ5smjJTG4IkpIDp++Q//7bj1P8PMRAZ5eMXRpy5GuLFUCAi2S4WGYwTPEkFEAKIAXQ4xKIVFBEA2v8Phb5JcVSUD6DbSQcwN+u/LHMPBeSrnCfba8BjeOXr6xkgRiSUPye7vgPcmaEFwq8hFMqfiZiRmDRdUsYsA7w4dH/w4j1gCGJpHi2KOLXzz2BUAApgBRA70sgIoCIBNZzNBgVtJv7b35J/mRZq5w9MyhHD3Xb+lpQIAbrAhkNJKocjBep4vd814cofh5kpLdPhk6fcfRrLF8akNyi61PUdawHbI+RvjD3AEIBpABSAP0pgvXi85TQqeBEizYSXCtoDfOK+uTbH3xCTQEdGR6Tlw6+44jXxWggxe/5dz+sih++Jt7Dae0e4s6RlHPQzPcvi/uzDFrlUPoIBZACSAEkN0ggU0ITgNTQ/LJStZIoMYe/X/0Dua2i4+r/214Ky+BFZxRiYDTQfyDKhzRPRP2Id3Fiu4dE56CSBZXxf5Y8FRRr+g5S+ggFkAJIASSpRLBRudvOkYizn2p9BREZnJqKQ7KntvKQ/PnyZ6773vE3z9i6DjAejAZ6HwjfgZ475Hf9VRwMH8gfKn46rd1DPEoXLUx6ATKmbQ7W8IWU27PCNX2EAkgBpACSDCUwKJFoYICjER+sEcQJGVdmKYPZg5TP797zD+p9LP29Q3Korctxr5fRQO+BaF9E/FZzfZ9fJpqK9PWfeNsV8pcs/TOWNRM/aWr8/FcauXUJBZACSAEkeiQQ6wERCdzC0aAMmsWmql/KpsALcX/2qxeOy/iYMydo7BvobrCer+3cCkb7fCp/Tu31F4+p7R+S0L5/c/VqbmFCAaQAUgCJESIYFEYDM5bBPLSW4JrBpKDwy3fv+VbCnzsxDXQqajQwMFPy8lgoyA1A+l49u1y9Z1EXyp/j50a5OVJR/b5MCpE1KBLYzC1NKIAUQAogMUICGQ3M8uSNNYN5xdNZTTQOWPeH9X+JcFI10GRgTeCKlZVSMauYG5XSRxwMCr64Rf4ACr9k2J82rNxWKxLItX+EAkgBpAASw0QwKIwGZg0azqOaaH5xse9TRT9Q0SFfW/2DlL93uK1L+nqHXPGe5t5UKstuncciMTYTTe+E9L3ev5TSRyL7hcMbvcc7X5QtWZTNnzYpAtjILU4ogBRACiAxUgIRDUQkkJVCdYBU0Vgh9Ft0cGrbh0Q4tRhMIlAkZtGSWVJVPZs7uYW83l8lv1Nkr02Rvo7B+RwQ4mr5yyL187rDpnKrYhSQUAApgBRAYoYIol8gmscHORr6QUQQaaL5JdMlr9jbqYTpRv+iuCkKGIVpoeYCyVOlr6+KUT7iKfkDMwKL9J4HGAUkFEAKIAWQmCqC0WhgBUfDOBAdxATAi0L4tyt/LGvmvJH277stChgL00INmMArchdWhA8RvtcV4YP8UfiIV+WvuHKe2mtWJ4wCEgogBZACSEyXQMgfooH1HA0KYTJSVf5MhNVRwHPTAtKdc5tyXyUXp81Vv4f/gxlXzkrZlTPq1wuvvC6FVy7JnCvh674/FVYLzVz2OgYq1a/Zm4/4Rf5Q8AWFXwxiqyKAu7gnEAogBZACSMwWwaBEooFBjoa5IGU0WkwGcog1hW4gVeXPRFhRERTSdyy3Vjpy1lyVvmyADEalsFCU+8nIPeT39vdNyvyF5b7ffyF1Z0cq1GjemeGZqugxskcof5VGPmRYEUA2uSQUQAogBZBYJoL1EokIMi3Uqs9Qbo7kFRVdjRLmFhY5rrBMttG/KB0nziu3c4a/LkT22nIfuhrhM5uSvBGpKu1Rv75tZsfVscENBJSf4Xe8IHiXxqdHxG4sEtmD4LFIC6H8XQ8u5JUvDZjx0OwLSCiAFEAKILFUAlkt1GYQFcxTJha5ihg6QQo3Vf1SNgVeyPrvx8cnpe3XYTUaaAQD0+bJL/K+aJn4ZUNVjAwW5w1LVdnp637+gYobo6Jzi/qvyqReUGjlBhFXRW76td/pu/Y7v+tnwIFQ/jKVvxlLFpt1bG5XBHA19wxCAaQAUgCJ1SIY0CSwnqPhgM9aTKQwJz9P/dqqnoQ/vPfvdUe2zp4ZlKOHunW/liO566Ut7yEZlRLuFIRQ/myjYtlSs1P4axUJDHEPIRRACiAFkNghgkHh+kDHAgnMVSYhuZoQ5kAUDSw2g3V/WP9nBHoKwkD4Xsj/oryTs4YbnRDKnyOOvaUL5pt5Ia5ZEcAG7iWEAkgBpAASu0UQ6wNrOBrOB1emcwuUW2GhTMvNVVNJp+XkZjxZ+fYHn7i67k0vSAFteyks42OTGcvfvoImtdgLIYTy55g5UG6OlC1aaGaF55lsCUEogBRACiBxggjWSyQiyNm4y+UQ95Fb3nX/jwLxgwAaSaYFYSB9kD+mfBJC+XMqqAKKaqAmwJYQhAJIAaQAEoogsU4Q//rekPzH971p6GMPDoyqBWEof4T4cKI4ManIX49cHhj03HszSQLZEoJQACmAFEBCESTWUFp4WZ76/E/VeyPl71DbybRSQCF9Txd8S1dfP0KIs+TvYudJmRgZ9ex7NEkCWQyGUAAdSg43P/Err+xY36zccIUSi9XDHBFv8JGqLkPlD60g3jjak7b8IfJH+SOE8mc2lYU9hj0WUltNeI+PcA8ihAJICEWQmM4nbn3bUPlD5G/wYnoTo/+d18CCL4R4BAjRhXfCjpS/P5jTKg9V/liKckYMe0wTRLe+bu+JCu5JhFAACXGLCLZzRNxHZdmg1Cw8bdjjHT92Jm35Q5+/Y7lBbgRCPCJ/EKLJsTHHvbZVZYfk7vKXpCKvTzZV/siwx0W0c/BUj3pvIBu4NxFCASTELSK4WvmyVrmFOCLu4RPLjYv+dXX2SU93etX+EPV7MY9trwjxAqjyCfkzWIQMAWmfiP5FWTK9Q9bN+qWh4otiNwbyOPcoQiiAhLhJBEPKDRIIGWzmiLhAAA1K/+zvHVKjf+nyi/wvcfAJ8Yj8YT2cE+UP6Z5/OPeZG9I+1818wdD1gKh0Onz2vFEPV1O390SAexYhFEBC3CaC7coN4R2khzbBDzgqzqNm4XtqCqheIkVf0k8jbct7iOv+CPEAED/cnAoif4lE7z/dtBfnJfTdCxvxXMNnz8n40JBRL51RQEIogIS4VgTDyq1RE0EWjHEYn7j1hCGPc+xoj4wMp7fuZ2DaPHXtHyHEvahr37q6Hd3gHWv+sPYvETPzeyta/vi7F7R17NGsFV0XKwe7DYuEch0gIQ6DfQAJ0cHaba1BiVzd5AnOZp7/wlO62z+cPTMoRw91p/37L+R9iYVfCHG5/Dm9xx+ifn968xNJf6eqeo5ym61+WTT/6bB2fkIFzi3aOSqrapxFs2ZKceU8I94GewIS533+2QeQEJIN2jrBjcL0UFvB2j+98ofUT0T/0qU75zbKHyEuBtLXf+JtR8sf1vs9vOAHSX8nLz9HFgVmRv+7J+b81B+TtdKUzfOP9PYZlQrKnoCEOAhGAAkxmLXbWuu1kx3twCJ21B1QG8Dr4ejhbjn7XvprCPflN6kSSAhxH9FiL04Hkb9UBV6Wr6yU+QvLY79VWzT/6VCcc1NAE8SMzk05+flSvjQg03J1xQz692+unsk9jzgJRgAJIYahtZFA9VBcdTVsUT6JDyJ/euUPVT8zkT+IH+WPEHcydPqMK+TvU/OeSSl/pTMKp8of2J7g3BTWzk1bM3kd6IWIojA6qajbe4JLJQihABLieRHEyXartigfaaItHBXj0St/mVb9HJkskrbchzjwhLgMrPcb6OxS0xqdTqqiL1FuuTXu+rzgSM+mYJJzEy5MolBMOO3jnjJmBqTKMg2UEAogIb6SwRZtrSBSYHD1tZ2jYgx/tOqYrr/vCvelXfWzf3ym/OjsnzH6R4jLgLxceCcsY5eGHP9a31/yxnXN3hOBdX8Vs4oT/Xh7inNSuyaBoXRf19B7Z/S+tQ11e09UcG8kxH64BpAQm1i7rbVGIldEkRYT4IhkDvr+PfXwT7P+e4jfSwffSet3T4/Ol/956guSWxmQwopyDj4hLsEt6/3UY1phj1r0ZWqz96mg8MuH1r1P8vKSXsePuxYwzrkI6wLr03l9JQsq9R7/GvZvrm7mXkmcANcAEkIsR2swH00RxboMnBRZRTQDPrJUX/rn8TfTu6Idlb/RacVSUFbGgSfEDZO7iUnHN3ePBdL3UOWPU8ofWL5yfir5A2mlXCrnIPS13ZXO7yIKqLM3INNACXEAjAAS4jDWbmtFRPBTEokMMl0mCYj+IQqYDSj8cqgttUD+/tIKefbMg+raP1z5xhVwQoizQcrn4KkeR7d4mCp/iPylKvoC5t5UKitXL0z3oa/2BUzj3FMvMW0kEjF97hzlNlvP263av7k6zL2U2A0jgIQQx6CtF2xQblgviHWDzcLI4A1Uz+nNWv7AW2lE/xD5i8ofKKyYwYEnxOEg5dPpzd2nkk7FT4DUT0T/MqA+g3MPzjUpK4SO9PaqlUF1wGqghFAACSGUwcxB8/ds6em+IIMXR1PKH9I+o/KHXlh5xcUceEIcSmzKp840RcvlD4Vf0qGqek46qZ+xZJRyqVUIbU41zsNnz+vYThOPc28lxF6YAkqIC1m7rTUo19JEA34cg+e/8JTaAzAbUPglWeXPqfIHimbNlOLKedz5CHEgbkv5jIJqn2j5kA4Zpn7Gsrpo/tMZVZ5OpzAMmsPnFhVm+9ZX799czWrYxFaYAkoIcRWv7Fgfiikgg1Levmotgd5/2cpfx4nzSeUP0veT05+9Tv5AwYxS7niEOBD0qEOLB7fJH/r8pSt/WaR+xpJx4RWtMEzSc4rOthAsBkMIBZAQokMGUU10l3KDCCJVFCfuZvFwquhHlp7M6u/Q9L2rszfp7yDyh35/sUzLzWH6JyEOI9rYfej0Gde9dsgfUj/TJc2qn4nIds0dqlOHE/0QPRXHh7Luq1jPPZgQ+2AKKCEeRus1GK0qWuOF94TIH9I/swHRv44T5xL+HAVfjgzcccP3C8pKpXTRQu5QhDiEywODculUj6vW+mUrf/MXlisCqLv6cMZpoDHnkAOSoCJ1fkmxlC1ZlO1r2rh/c3UL92ZiF0wBJYR4Ei062BgTHYwWkgm79T0h/TMbUkX/IH7x5A/klTD6R4gjJmyK8A12das3P8hf0fR8WbbckLXHwWzPIRLJKokLooCQ8SxhGighNsEIICE+Ze221oA2KVgnLuo5+INNz6stIDIFTd+7wn1xf4aiL99790sJ/1ZnsQNCiAG4OeoH0OYBvf7SafQeZc2HA1JaZsixJ1Q0/+laHeeLncrdlng/Q4XkimVLs33omfs3V7OyNbEFP0cAKYCEkOgJviZGCPF1wHETqLJBtfl7pqDoCyp/xv3ZZJF8r+tLN6z7u3qsyM2Rme9fxh2EELsmaWp7hx49kSZXyh9aPlRVzzbsNSgCqGvio5wjDkuCpQQlCyqlsKI8m4fdqgjgLu7lhAJoLXnc/IQQoKX64LZLO9kHYoQw6AQh/KNVx7L6O6z9SwTW/SWSP/UgWVTEnYMQm3B71C9b+Zs5q9hQ+QMjPZuCigSGdDwElhBAAm/IFkFfwCwF8JHoOYcQYh2MABJC0kIRwgpNBGtipNBSsun9lyz6hzV/EMBkTJ87R7nN5g5AiIVMjo2pDd2xxszNZCN/aPnwoXXv01P1MxFNigA26jwPYLnAvng/0xEFZE9AYguMABJCSApe2bEe6zRatFt0MhBNG12liaFplUY/cevbWfX+SxT9Q9Tv5+fWp/z7nHweJgmxEvT1Gz57ztVRP/D+kjfUgi+ZyB+4Y81iM+RPtOO03vNAi3Lcb5Y4bRx0RAEflySFZgghFEBCiLOkMJo2KjFSGNRE0FAphABmPJEcHpOe7gtxfxav2Xs8cgvyuaEJsQD0lLt0+ozrGrrHNa0Mq31GQcVPg4q+xMOoC3RbJc6yAERtR/svZCOBG+r2ntjKYjCEUAAJIe6VwpByF0oihQHJMH0UxV9qFp7O+LUkiv4d7PuoWvkzrYMkG8ATYiqI9A29d0aVBy+Qrfyh39+iJTPNfGkBg47x/coxHRG7A1N/hu1YUFamFs/KACwvqBeuBSTEMrgGkBBiC1r6aGCKGMa9Qv23H/11xhHA/t4hOdR2Y8/AVC0fpjJrxfu5sQgxCa+ke+qVv9IZhWamfsZSq7MQTOwxvFG52z71+1mumw7v31xdxU8EsRK2gaAAEkIcKoblRaOBH39uX02m6/8OK/LX13t9AQmkfP7PU19IO/qXX1IsZUsWcaMQYjBeSveMsm7WL2XdzBcy/jsUfVnzoYDa9N0CGhQBbDbweH1DawhE/yqq35dpFFCVU0UCQ/x0EAqg+TAFlBDiKGLWFarFZkZ6Nm2RDNeuIPo3Vf7Awd70Uz8JIcaDdWJDivi5uadfPBD1Q/QvGxD5s0j+QMBooZRIa4hrk+qJSTWym0UUEMVgKICEWEAOh4AQ4nAez/QP4q396xyuklcvfIijSYgNqOv8FPHrP/6Op+QPFT71yN/ylZVmFn2JxxIjH0y7YNc09fsjvb3ZpPWiGEyAnxZCKICEEB8z0rMJPacymhAkiP71Hx1chSbGG7XJCm4h7Zaw8lxuYSE3AiE6xQ/tAfpPvK1GhbwE5A89/rKVv6rqOWrhF4sxXLAUCWyUKdWgo1HALNjOTw0h5sMUUEKIk8k4+vfWm2fifbvp//mvjdH+hS3xfkFrdF8TM0kK5BVPt6XhPSFeAFU9IX9I+/QaaPD+h3OfUe+zAeJXVT3bS0NyQyooivsUVsyQnPyM0lvZEoIQC2ARGEKIIxnp2QTxOpDJ36Dn37GjN7SLCNU1tNdm8xqUiUij8Io0IRS/GALTO+Shyh9l3OA9ysxZxbJ6jW3FpfqL5j9tSq+JeFVB0ROwZEFlpg/VpAhgIz9JxGz8XASGKaCEEKeSsXjFWfuHq8gNHEpCrBE/rPG7dOq0Z+UP6Z5I+8xW/tDuYeUdC+18CxVmPXC8VFDsE1nsC4/X7T1RwU8UIRRAQoiPGOnZFJAMUy+7OvtkZPiGiUZTXUN7mCNKCMVPLyj2kk2Pv1j5s6jXn53ccMEN+0UWkrqFnyxCKICEEH+RUfRvfHxSOk6cm/ptpH7u0vk6uA6FEJ+LH6J9j+go9gLQ688H8he3KujYpSG172MmXJmYeJyfMEIogIQQn6BF/+oz+ZuucJ+Mj01OFTcjUj/buUUIiZ2Ya1U9fSB+AEVe/nTRE7JkegflL30JbJx67MQ+kwnTcnMr6vaeYBSQEAogIcQnZBT9Q9pnnOgfUz8JMZBoA3e0c0B1R6+LH4iu96vIy759RVT+LO71l/yYGSmwZTbXXYBDFBAR40zPBVwLSAgFkBDicbSJSX0mf3P8xrYPRqR+RqFEEl+D1D1E+hDxQ1+3LJp7u5Loer9si704Vf6sIl4qKKKAGe4/XAtICAWQEOIDMor+oen72fcGr/uWGFj1c//magog8SWI1lx4JywXw13ZRG5cC6J9f3rzE7rW+/ld/mIksFG5C0X/j6hxFs3hWRGUEAogIcSraNG/YCZ/E6fpe4MJqZ9cB0h8QTTNs+/3x9Wo38TIqK/e//tL3lDX+2Xb3D1K0fR838tf7DFZYoppZZE+zCggIRRAQoiH2ZnJL6Ptw+DF6yaoLYr8tZjwuiiAxNMgwjfQ2eW7NM+rwpYzoqZ7bqr8sa6UT4BWD2s+HKD8abyyY31Yudsa+z1cZMgQrAUMcDQJoQASQjzESM+meuWuJt3fj9P2AZMMsxq+H+EWIl4D0T1E+aLRPhTp8COI9j2ss8VDrPy5odonUuctlsBm5e7qxbnLA4PqLUN28lNLCAWQEOId+avI9OR+7GjP1LYPSP00q2dfC7cS8QLRNViI9GF9HyJ/fov2xXJ3+Uvqej+9KZ9g7k2lrmn1UHnbcyEbnhYX6MLR/yAKmOG+t6Fu74kgP8WEUAAJId4AhV/SXuQfp/ALWj6YNqHRCsGEuZmIm6UPwgfxw8TbDy0ckoFCL2js/gdzWg15vPkLy2Xl6oW+6fOXDa/sWH9dgS7sg1gPmCGMAhJCASSEuJ2Rnk1I+0x7gT9SP984ejr2W2j50GjBS32SW4u4Wfr8VtAlEWrUT2dj91iWr6xUbyQtCQxJTGsI7KMZ7pc1dXtP/P/snVtsW/d5wD/xIt50oWRJjpw6opM0sYE5URsgTTt0UrBhBjxgtoABHZqHyBiyh2FY4oe9DAGSAO3LMCTx0GF9i/NSIDO2eljTDV1TMwXcFH6oZWO5zE1jOrZsT75RN0oyddn5Ds+RSJqkeCRSPDz8/YCDw5so8s/Dw/M73/f/vtcZSQAEEACam3ecPFjn/Wnjdws9ozy2Q6/zZCunyoH70QNp7bOG9JUmP+q33UIvSq7Nw14z+geOJFAFLmlfn7vuOP32ZQrCACCAANCkLN74jkb+qi78oqmfV1MFPaTG6jjvrwBNA527dv00EghuQbdFLaRhN2lX8dOUOqTvQWod9TMrfX4rIfHeaDMOhxuqGuuJu5ResE9cOHF5cXjiEAAQQABwh/wlxEHT9xKpn8frOe+vFNn5+RMzV76U5UyGDxAagn2wrC0btHrn3NVJs5BLq8/pK2sKNY76KXsTPab8aa+/JiXd6BdgzQdcz97YwomL0cM/+pzegADboG1tba0133hbG58+QOME8Iw4aPr+qSF/Nyan7asnDfk71ojX/dyr72sIIRGKd0u4t0f8YXp9QX2FL5vJyPJ8xlwTga6ekd5fyDe6z9ZM/DTl88DBQekf6Gj2oTkZHnzvmBteiLE/HRcrmucLBqX70YS0+auOS6hEfs0q0gWwJVrVgcx9Gh8/AOyw/L3uRP5uTc3ly5+mLx1v4MvXAgbvaNRFFxVAFcH2zk4nBy4ADx6IGHKnkqfSp1HmVu3Lt10Skcvyx7ver0lrB5ue3qhZ6KWJo375XHHLC9H+gIYEjhgXxzWKnfm/KYntqbqgjp0K+jxbPYBziAACwE7Kn875O1/14xeycu5XKbvnn57x3bdT8/7KYUcBi29XGVQRbO/sIDIIm8reytKiIXkLhvAtyrIhfaRxbg+N9GmqZy0autto1G/f432yd6jHS0M1Fh58z1W9TY196npGiAqgZlg44PhPv/v423wDYEv7YiKAAAB1lz89Y/vjah+v8/4unp/Ml7/nGy1/FmYUsPhGc36WOUfrthkNDITDEohGJRiLiD8UJkLYwqK3cj9rCN6yGdlbNoSPVM7aokVeRno/qFm6p+KxqF8+KTdKqbGoBA5rFFD3nQ5Oor11+EefJw0JnOCbAFA9RAABYKcEUKVpvNrHF83704qfrjlrXS4KWHGfkyeFvmBA/O1BxNADaOROF1vy7OuIXv3RdM8/HfhXs9hLrfDQXL+ShAffc+XBj7FP1f2pZofEVf66hh5xsm9UqdX5gGm+FeAEIoAAAPWVv3En8qfilyd/x9wkfxY6D/HHTv7AnOM1X3puVzAWlTafT/yGIOauR3I76GiUjadBaER3bXXFvKypmrnPcEVWlnLVChG8xqHCd8QQv1q1dbAx0z0TPRIIePakTNKtL+zX3/uTlCGBOp/vjPHdi89fvyEdex+u+lyA5LIyxvh2AFQHEUAAqLf8OZr3p/3+fnPuar78nXTj+8qft1JvtEKeRgwVfygkbX5/7nI4JD7rLHmbz8/cwxLSrSmY+dgyVyx0ufsovOJmNMVTUz015bOWaDP3fY/v8mK6ZzFvhwffO+7mF2jsV/X3Qvet8Uh/n0T6dzn5c+YDgrPfiBaOACKAAFBP+dN5f3qaPl7N4+dmlwz5+9Ke99ewdg8ODlTOu/X12SmnBbflRRmLyZfJqv9HFdK51b6JWhilXITNTrMsBoHzrvh9I/6rmrZ1sPnqgQFzvl9Hp/dPnkzN/+Hpu5nn3jUuTgw/9VTKxfvWUUsCt1IU5nlDApN8awABRAARQIA8Ji5eVBkb3sKfJsTBvLegf1oe6/3BkWr/lxZ9OXc2ZVb+jPQ8m+559K9POHlb4rzBcdo4CNpW4QDjQOUtY0VDYoA6oVU9a9nIvaJoRoISMZawtXR0hSQY8K1fb2Z0/3o5/beyslZwAihp7TsvSOXiMI72/bXgZ5/NHvm3i2nzt0P7AzrIbkg/27t87Oie+xV/D4x9P5IICCACCOBKKSsnat0VpGqrcldzBjv/Q7rDF6s+ONHI39zMkkR3fVviiZfc8tGkrQOkkvfdy6yk/uHM1Ct35pfZiAFqLH7azL2WBV5qJYjmjrY3at0WWL+toyvsqvmDul+dm1k0e6nOLj0p0T1/1VTbwEepeXn33F0zm0GLwlQrgYPhVXlp35KE/ds+vq0kifq7MF3N3yCbCCACiABC60hcsYg9LYVpkMNSZVpkM7K747+lJ3LOsfx1731BYgOHmuq9Xrq1JG+emeILAOBR8duuLNrXi6OIWnG0cxuppwsLWVlc2Dj5tGhez6VG37tbmA7djPtW5Vo6a+5fF1alURJYD1JSGHHVy1dKSSTyiAAigAggNFbuRq2Lo0VC55qIm1vQqJ9G/5zKn0b9NPrXjJyaSMsHl2b58AFaXPzcykPDPxSfvzmrCm9VAr/esyx/9vB9L32MySJhtDNUtj2dAQFEABFAaHXRG7Ykb8gSO09H6twgf5l5v3TtfaFp5U9ZyK6aByhX01k2AoAq0Xl9T8Y+QfzqPc7xZ6T3sZeb+j2oBP7z2dtyd3G11SWwEilr+dBaJ91c7AcBRAARQGi09KnwvWgsR5G9nZe/XU/8nQSjjzT9+7fPUmey9IYD2Ez86lXVEx6kz9jHtnfub/r3YZ9ouza7ggQ6k8KksbyBDCKACCACCIUCuMYobI/O0CV5uOtUVY/VOSoXz0/K0vJuU/6aNS2pFHbRAgB4EI3yabRPo36I387gb++T3Qff9NR70n3sr68uSGzPoCG2HUhglSJoCOA+vhEIoE2Ajx9AxozlNWEu35blr9rIn93nr73r96X/qy95biy+mYiZkUDmAwJskIhcNpu3q/jBDu+f94x57j29+GyvPDGgJ9smq+4T+Jt7ucPdFpXA08Zygm8D5EMEEMBi4uLFhGzM+xsR5v9tipO0zxuT0/K7385L9KE/b+r5ftXww7O3ZWJygQ0EWhbm9zUeTa3vP/A9z74/e17gXDBmimA1tEAkMCUb8wC1MIzOA0zzbSgNKaAIIEAlMRy1LtrrEWvd0oLoRP5++9mU3JzqlN7HXjFTkrwORWGgVVHZ0/l9WtWTNM/G4pW5f5vta3/y8Ywkv7xvzgvUnoEel0Bb8FTqLli3JYVKoAggAogAQkMlMV8Ulfz+f55pGVGt/Nnz/do6Dkvn4FhLbRNIILQSKnzDxjIUucxguADNstDWOq3ChckFOXVxRhbj/VXNC3SRBCbzLudLXf59yB0CiAAigOBhcawkiSNlnmLHo5DVNnm/euWeXL/ZLx1f+YuWiPohgdBqPBS6sT63j2ife9DCWgMH3/RUga1q97caDTx7OyCR/r5No4FbaBafksIG7uXEbf0n3rpPEDkEEAFEAAEaKZjlSFhLWQK+me7dHT8f7wx9WlE4Ner32f/cTGdDhya2GfUr96NaDdrHcRwJBKgtmuL5ZOxTM+KnAgjuowlTP5M13PebEvifny+OxAYHRgPRyhLc276WPrT7/vGD3SspBA0BRAARQADIl7ob31HpOyObpLBe+eJuevJq+oQhgW8fPjbRsInnhvjqax11y/ghgdDM2AVd9hviRyVPd9O99wWJDRxqtpc9ZojX6Vo/6XOvvj/e3t31WnSgL+ELBis9VH+rnv/pdx9H/hBABBABBABL/oYt+Ssb+dMKn9eupE/Oziweb6T4WfKnr/e828ZRJVD7V1EdFJoFW/o02gfup4nn/Wmlyufr9eTfeuNnr4d74i+HeuLxTdJCjxkSeJItCQFEABFAgFaXv3Fj9U65+w3hS9+8PnPyaureCUP8Um54zYYAvmKs3nLrmJ4y/Jg+geBGNNI3FPliPdLHvD7kb6cwBLCuB2XPvfp+3B8KHY3u7n8t2BFLVHjoSUMCj7FFIYAIIAII0IriF7ckarzU/Xduzadmphffvfz5bUepnlZ0rlQkMSGbzEG00I6/m1VSdX211Y9S83LqfFoy2VU2Nmi49JHeifw1GP0N2axReUrKFGBxOm/vD/7+l+PtXZ0vBmOx0TIRQX2+MUMEU2xdCCACiAACtIr8qTy9UyxRy8urWuDl9LUv0+/KwD+my8jWSDOJWCO5M79sNoxnXiDsNFq8ZSh82ZC+T2jbgPx5kWJZVKGbzrts/n79zX+l08FY9GVDBo+2+f3xElKqKaGnGU4EEAFEAAG8Ln+aPvma5EXp0rO9Mr/yNZle+L2UL9CRYJRqi1as+8nH0wwE1A07tTNhyJ5W8NRKntD8qPipAML2hfHczeXE/y6E5ZOZQHH7iLeN5Q1DBNMMEwKIACKAAJ7i2u/+KdEX/aWmfB7V63NLTxjCt9dcr/l6GaB6j386K/8ycU8uTS0xGFATutoWZMA3Lb1ts3Iwfk66wrekM3SLgfEAwegjEh/6S3MNtUWLdX0y45fLi0FzvbhiHiumHo2tHvvBkSeSjBACiAAigACe4PoXb74VDtx8ZWl5t2SyQzJrSB80BuYGwnaEr7dtzhS+Xt+cBGSl9OMsEUQImxNt8dC5Z6zlmrw3ihuLPvn4XpukDCHsDq6e/v7h/WOMCgLoBQJ8/ACtzdTcH5F/6BK+mYjJ8MMR+eDSnPzi0iwiCGUxZc+XEz6Vv3LCV8zMYr+5TE4jhM1EqPOAdH3lBaJ+O8xgeFUGB/WS+f1Kf58hAY9ABBAAtDpnQnLpn1rEZVQq9PyDnUFTkRBBUCJt903h62rLmOvOtvr1krRFMNqeli5j7fdRpKjR4tc5OCbtnfsZjJ1H5/1p0Zh/N5bTw089lWJIvAUpoAggABQKoV3B027bYFf3HGV0dl4EtXm8iiAVQ1tD9jSi12mmdDqL7tVFQAKZdSGMGQtRQsTPgyTtnz7JVQvV6ymEDwFEABFAACgUxIRs9O3L7+03JIX9/Mr1/YMtoMVidJ7gR5fniQp6AI3m5YQvYwpfo2WvWjRKGA2mDSmcttYUSKwFOq8vsuvb0rH7kPjb+xiQrWFH7fKvXyghe477BwICiAAigACwdXksJ4Vb6Rv4dJWCWXwQUIw2mD8q1TWjd5UMXppaJDLoYoKG0KncqejlUjlnJSK5y15CJTAanF6PFKoYkj5anfSF488Yy9fNtRd28db+dqv74lKkpHQTeDEkLslWBAggAogAAsB25fTFZpNBbSp/6daSKYVX0/dpJ9EgyQu2WbInS+upnM0Q0asXKoC2DLYHMoihhaZ3ampnuPsZrxR1UQljnhwggAggAggAnpBBFcEj4jwy2XBUBjVN1JbBS7cWLVlcMYURqkdTNRU7iheU5ZzwWeIHztE0Un9b1owY6jzDUGBe2v25tadODhiC52/vN6RvvwQjQ16Z06dRvNPG8qElfeQAAwKIACKAAOA5GdQ001HZqJI67IX3pSJ4J5OLUC3cXy1IJbWFcf26h6KKttDlS515sG6JnXm7B9M0mwVbCG1BVHQd8GULbnMLOl8vEOo31/5QnyF6j4jPH/NaAZek5KJ8SebOAQKIACKAAIAQekQIqyGbzcr09IwsrLWbApnJZMzb9Ta97+5ah3lbJlM+Mja7FpHsmt/R/7XTKythp15WEj7wDnaKqU2pCGLxY9a3p2BQuru7Kz5/QEUuUNhwPdRxYOP/ebdCZ9oSvguW8CXZ2gABRAARQACAB6Vw1JLBpy0hTDAqOW7fvlMkkNMb1+/nhDIfvV8fB1CJvr7CSpnRaESisWje9ai52HR3d5niBw/uvvKEb4IIHyCACCACCACwNSG0q5oihTUgJ4WFcxeLZbJAOm/dKftcuQhlhkGtI8Xy9YC89e9y9Hd9fbsY1NqQtITviiV7SYYEEEAEEAEEAKivGI5aMjhkremV6FLyI5fO/u52U7w/TYHcSkQMGWsKUpboXbDWKSJ7AAggAogAAoB7pDCeJ4O2GCaEiCEAbLL7sGTPFr00UT0ABBABRAABoLnlcFRyEUJbDhNC1BCg1SRPC7N8aK3tiF6KoQFAABFABBAAWksObREctW4asdajjA5A05DKW67kX0fyABBABBABBABwIoi2CNqiaEcQ7YgiANQXO2In1npaNiJ6CB4AAogAIoAAAA2TxIRszDkcKXEbABSStNYqcVeKb0PuABBABBABBABoZlHMn3eYf3kk72HMTYRmJmUtxVKXf7u2TkgzVAAIIAKIAAIAQKEwJmQjeliccvp0kSgijlAvkTM3R8mlXir5KZkIHQACiAAigAAA4AJ5LBbCfJksJ5GIpAc+ekvQpIy82SSLH4PEAQACiAAigAAAYAvlaJm7NiuGMyTVzYH0UlGd4ghZJT7c4vMwPw4AEEAEEAAAAAAAAOrN/wswALznJmMRLn+IAAAAAElFTkSuQmCC"

	@unittest.skip("The library currently only supports strings")
	def testEncodeBinary(self):
		bin = base64.b64decode(self.pythocat)
		base = ft.base64(bin)
		self.assertEquals(self.pythocat, bin)

class base64_longstring(unittest.TestCase):

	def testLongString(self):
		a = base64.b64encode(longString)
		b = ft.base64(longString)
		self.assertEquals(a, b)

	def testSmallStringDecoded(self):
		b = ft.base64(longString)
		self.assertEquals(longString, base64.b64decode(b))

	def testSmallString_2(self):
		a = base64.b64encode(longString + "!")
		b = ft.base64(longString + "!")
		self.assertEquals(a, b)

	def testSmallString_3(self):
		a = base64.b64encode(longString + "!!")
		b = ft.base64(longString + "!!")
		self.assertEquals(a, b)

class base64_utf8(unittest.TestCase):

	def testSimple(self):
		a = ft.base64(u'this is a test written when it is -20° C snowing outside, and i am going back to 中国 in 2 hours from øslo.'.encode('utf-8'))
		b = base64.b64encode(u'this is a test written when it is -20° C snowing outside, and i am going back to 中国 in 2 hours from øslo.'.encode('utf-8'))
		self.assertEquals(a,b)

	def testNotSoSimple(self):
		s = u"甲馬營中香孩兒，志氣倜儻真雄姿。殿前點檢作天子，陳橋兵變回京師。".encode("utf-8")
		a = ft.base64(s)
		b = base64.b64encode(s)
		self.assertEquals(a,b)

	def testSimple_2(self):
		a = ft.base64(u'this is a test written when it is -20° C snowing outside, and i am going back to 中国 in 2 hours from øslo.!'.encode('utf-8'))
		b = base64.b64encode(u'this is a test written when it is -20° C snowing outside, and i am going back to 中国 in 2 hours from øslo.!'.encode('utf-8'))
		self.assertEquals(a,b)

	def testSimple_3(self):
		a = ft.base64(u'this is a test written when it is -20° C snowing outside, and i am going back to 中国 in 2 hours from øslo.!!'.encode('utf-8'))
		b = base64.b64encode(u'this is a test written when it is -20° C snowing outside, and i am going back to 中国 in 2 hours from øslo.!!'.encode('utf-8'))
		self.assertEquals(a,b)

class base64_string(unittest.TestCase):

	short = """Abstract
    This PEP proposes to introduce a syntax to declare the encoding of
    a Python source file. The encoding information is then used by the
    Python parser to interpret the file using the given encoding. Most
    notably this enhances the interpretation of Unicode literals in
    the source code and makes it possible to write Unicode literals
    using e.g. UTF-8 directly in an Unicode aware editor."""

	def testSimple(self):
		a = ft.base64string(self.short)
		# Python inserts only \n instead of \r\n as defined by standard + attaches an extra line
		b = base64.encodestring(self.short).replace("\n", "\r\n").strip()
		self.assertEquals(a,b)

	def testLong(self):
		a = ft.base64string(longString)
		# Python inserts only \n instead of \r\n as defined by standard + attaches an extra line
		b = base64.encodestring(longString).replace("\n", "\r\n").strip()
		self.assertEquals(a,b)

	def testLong_2(self):
		a = ft.base64string(longString+"!")
		# Python inserts only \n instead of \r\n as defined by standard + attaches an extra line
		b = base64.encodestring(longString+"!").replace("\n", "\r\n").strip()
		self.assertEquals(a,b)

	def testLong_3(self):
		a = ft.base64string(longString+"!!")
		# Python inserts only \n instead of \r\n as defined by standard + attaches an extra line
		b = base64.encodestring(longString+"!!").replace("\n", "\r\n").strip()
		self.assertEquals(a,b)


if __name__ == "__main__":
    unittest.main()

