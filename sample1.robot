* Settings *
Documentation    このテストソースはコマンドを実行するものです。${\n}
...    case1:touchでファイル作成を行う(ファイルができたことの確認もする)${\n}
...    case2:rmで作成したファイルを削除する(ファイルが消えたことの確認もする)
Library    Process
Library    OperatingSystem

* Variables *
# ファイル削除コマンド
${cmd}  rm  ./hogehoge.txt

* Test Cases *
case1
    [Documentation]  touchでファイル作成を行う\
    ...    (ファイルの有無の確認もする)
    # 基本的にpythonのsubprocessみたいな使い方
    Run Process  touch  ./hogehoge.txt
    File Should Exist  ./hogehoge.txt

case2
    [Documentation]  rmで作成したファイルを削除する\
    ...    (ファイル有無の確認もする)
    # 基本的にpythonのsubprocessみたいな使い方
    Run Process  ${cmd}  shell=True
    File Should Not Exist  ./hogehoge.txt

case3
    [Documentation]  ライブラリを使わずにkeywordで${\n}
    ...    case1,case2を行う
    ファイル作成  ./hogehoge.txt
    ${out} =  ファイルの有無を確認  ./  hogehoge.txt
    Should Be True  ${out}
    ファイル削除  ./hogehoge.txt
    ${out} =  ファイルの有無を確認  ./  hogehoge.txt
    Should Not Be True  ${out}

* Keywords *
ファイル作成
    [Documentation]  ファイル作成を行う関数
    [Arguments]  ${filepath}
    Run Process  touch  ${filepath}

ファイル削除
    [Documentation]  ファイル削除を行う関数
    [Arguments]  ${filepath}
    Run Process  rm  ${filepath}

ファイルの有無を確認
    [Documentation]  ファイル有無を確認する。
    [Arguments]  ${dir}   ${filename}
    Log To Console  ${\n}  [exec cmd]ls  ${dir}${filename}
    ${out} =  Run Process  ls  ${dir}${filename}
    Log To Console  [output]${out.stdout}
    #　文字列の比較には変数にもクオートが必須!!
    ${res} =  Set Variable If  '${out.stdout}' != ""  True  False
    Log To Console  [result]${res}
    RETURN  ${res}
