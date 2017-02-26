fomatter = "%r %r %r %r"
print fomatter %(1,2,3,4)
print fomatter %("one","two","three","four")
print fomatter %(True,False,True,False)
print fomatter % (fomatter, fomatter, fomatter, fomatter)
print fomatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
