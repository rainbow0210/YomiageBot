import re
import subprocess

def creat_WAV(inputText):
    #message.contentをテキストファイルに書き込み
    input_file = 'input.txt'

    pattern = r'<:[a-zA-Z0-9_]+:[0-9]+>'    # カスタム絵文字のパターン
    inputText = re.sub(pattern,'',inputText)   # 置換処理

    with open(input_file,'w',encoding='shift_jis') as file:
        file.write(inputText)

    command = 'C:/open_jtalk/bin/open_jtalk -x {x} -m {m} -r {r} -ow {ow} {input_file}'

    #辞書のPath
    x = 'C:/open_jtalk/bin/dic'

    #ボイスファイルのPath
    m = 'C:/open_jtalk/bin/nitech_jp_atr503_m001.htsvoice'

    #発声のスピード
    r = '1.0'

    #出力ファイル名　and　Path
    ow = 'output.wav'

    args= {'x':x, 'm':m, 'r':r, 'ow':ow, 'input_file':input_file}

    cmd= command.format(**args)
    print(cmd)

    subprocess.run(cmd)
    return True

if __name__ == '__main__':
    creat_WAV('テスト')