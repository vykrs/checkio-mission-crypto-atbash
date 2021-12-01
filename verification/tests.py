"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ['testing'],
            "answer": 'gvhgrmt',
            "explanation": 'Basic'
        },
        {
            "input": ['attack at dawn'],
            "answer": 'zggzxp zg wzdm',
            "explanation": 'Keep the whitespaces'
        },
        {
            "input": ['Hello, world!'],
            "answer": 'Svool, dliow!',
            "explanation": 'Keep caps and punctuation'
        }


    ],
    "Extra": [
        {
            "input": [''],
            "answer": '',
        },
        {
            "input": ['''The Atbash cipher is a particular type of monoalphabetic cipher formed by taking the alphabet 
(or abjad, syllabary, etc.) and mapping it to its reverse, so that the first letter becomes the last letter, 
the second letter becomes the second to last letter, and so on.'''],
            "answer": '''Gsv Zgyzhs xrksvi rh z kzigrxfozi gbkv lu nlmlzokszyvgrx xrksvi ulinvw yb gzprmt gsv zokszyvg 
(li zyqzw, hboozyzib, vgx.) zmw nzkkrmt rg gl rgh ivevihv, hl gszg gsv urihg ovggvi yvxlnvh gsv ozhg ovggvi, 
gsv hvxlmw ovggvi yvxlnvh gsv hvxlmw gl ozhg ovggvi, zmw hl lm.''',
        },
        {
            "input": ['ATTACK AT DAWN'],
            "answer": 'ZGGZXP ZG WZDM',
        },
        {
            "input": ['$1000000'],
            "answer": '$1000000',
        },
    ]
}
