def extract_words(text):
    return [word for word in text.split() if len(word) >= 4]


print(extract_words("Don't judge a book by its cover."))
# Output: ["Don't", 'judge', 'book', 'cover.']

print(extract_words("All that glitters is not gold."))
# Output: ['that', 'glitters', 'gold.']

print(extract_words("The multinational corporation's decentralization strategy required comprehensive reorganization of their compartmentalized departmentalization systems across intercontinental subsidiaries."))
# Output: ['multinational', "corporation's", 'decentralization', 'strategy', 'required', 'comprehensive', 'reorganization', 'their', 'compartmentalized', 'departmentalization', 'systems', 'across', 'intercontinental', 'subsidiaries.']
