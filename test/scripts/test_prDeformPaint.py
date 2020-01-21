import maya.cmds as mc
import prDeformPaint;reload(prDeformPaint)
prDeformPaint.Ui()

testFile = '/home/prthlein/private/code/prmaya/test/scripts/test_prDeformPaint.ma'

mc.file(testFile, open=True, force=True)
mc.file(rename=testFile.replace('.ma', 'TEMP.ma'))
mc.file(renameToSave=True)
prDeformPaint.reinitializeMaya()

#prDeformPaint.initializeMaya('/home/prthlein/private/code/prmaya/prmaya/plugins/prMovePointsCmd.py',
#                             '/home/prthlein/private/code/prmaya/prmaya/scripts/prDeformPaintBrush.mel')
#prDeformPaint.reinitializeMaya()


