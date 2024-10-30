# Task_308

myStr = ("If thou should live three thousand, or as many as ten thousands of years, yet remember this, that man can "
         "part with no life properly, save with that little part of life, which he now lives: and that which he "
         "lives, is no other, than that which at every instant he parts with. That then which is longest of duration, "
         "and that which is shortest, come both to one effect. For although in regard of that which is already past "
         "there may be some inequality, yet that time which is now present and in being, is equal unto all men. And "
         "that being it which we part with whensoever we die, it doth manifestly appear, that it can be but a moment "
         "of time, that we then part with. For as for that which is either past or to come, a man cannot be said "
         "properly to part with it. For how should a man part with that which he hath not? These two things therefore "
         "thou must remember. First, that all things in the world from all eternity, by a perpetual revolution of the "
         "same times and things ever continued and renewed, are of one kind and nature; so that whether for a hundred "
         "or two hundred years only, or for an infinite space of time, a man see those things which are still the "
         "same, it can be no matter of great moment. And secondly, that that life which any the longest liver, "
         "or the shortest liver parts with, is for length and duration the very same, for that only which is present, "
         "is that, which either of them can lose, as being that only which they have; for that which he hath not, "
         "no man can truly be said to lose.")
myCount = myStr.count(".")
myCount+=myStr.count("!")
myCount+=myStr.count("?")
print(myCount)
count=0
for i in myStr:
    if i == "." or i == "!" or i == "?":
        count+=1
print(count)
print(ord("."))