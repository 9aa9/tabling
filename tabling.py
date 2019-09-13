'''
$ Email : huav2002@gmail.com'
$ Fb : 99xx99'
$ PageFB : aa1bb2
'''

def TABLING(lines):
    num = len(max(lines))
    nums = [0 for i in range(num)]
    for line in lines:
        for a in range(len(line)):
            if len(line[a]) > nums[a]:nums[a] = len(line[a])
    for a in range(len(lines)):
        lines[a] = [lines[a][b].center(nums[b]+4) for b in range(len(lines[a]))]
    lin = ['']*len(nums)
    for a in range(len(nums)):
        if a == 0:lin[0] = '+'+(nums[a]+4)*'-'+'+'
        else:lin[a] = (nums[a]+4)*'-'+'+'
    for line in lines:
        print(''.join(lin))
        print('|'+'|'.join(line)+'|')
    print(''.join(lin))
TABLING([
["name",'suname','age'],
['rahim','rahim','17'],
['ali','ali','16'],
['','','']

])
