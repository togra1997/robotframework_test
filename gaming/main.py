# データ処理クラスをインポート
# フォルダ構成などは自由にいじってください
from .csv_manager import CsvManager
from .parquet_manager import ParquetManager


def create_sample_data()->None:
    """サンプルデータを生成する"""
    # リスト形式のサンプルデータ
    list_data = [
        ['名前', '年齢', 'スコア'],
        ['田中太郎', '25', '1500'],
        ['佐藤花子', '30', '2400'],
        ['鈴木一郎', '22', '3200'],
        ['高橋美咲', '27', '2800'],
        ['伊藤健太', '35', '4100']
    ]
    
    # 辞書形式のサンプルデータ
    dict_data = [
        {'名前': '田中太郎', '年齢': 25, 'スコア': 1500 },
        {'名前': '佐藤花子', '年齢': 30, 'スコア': 2400 },
        {'名前': '鈴木一郎', '年齢': 22, 'スコア': 3200 },
        {'名前': '高橋美咲', '年齢': 27, 'スコア': 2800 },
        {'名前': '伊藤健太', '年齢': 35, 'スコア': 4100 }
    ]
    
    return list_data, dict_data

def main():
    """メイン処理
    ここは自由に変更してください。
    """
    # サンプルデータを生成
    list_data, dict_data = create_sample_data()
    # インスタンス作成
    csv_manager = CsvManager()
    parquet_manager = ParquetManager()

    # listデータのcsvの保存処理

    # 辞書データのcsvの保存処理

    # データ処理の取得処理

    # listデータのparquetの保存処理

    # 辞書データのparquetの保存処理

    # データ処理の取得処理


