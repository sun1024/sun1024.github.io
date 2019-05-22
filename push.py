#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system('hexo clean')
os.system('hexo d \-g')
os.system(ur'git add .')
os.system("git commit -m 'Updated'")
os.system('git push origin hexo')
print 'Over!'