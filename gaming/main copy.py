import os
from pathlib import Path

# 各レベルのデータ処理クラスをインポート
from easy import CSVDataManager
from hard import CSVDataManager as PolarsCSVDataManager
from normal import CSVDataManager as PandasCSVDataManager


def create_sample_data():
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


def process_with_easy(list_data, dict_data, output_dir):
    """Easyレベル: CSVモジュールを使用したデータ処理"""
    print("\n=== Easy Level (CSV Module) ===")
    
    # 出力ディレクトリを作成
    easy_dir = Path(output_dir) / "easy"
    easy_dir.mkdir(parents=True, exist_ok=True)
    
    # CSVDataManagerを初期化
    csv_manager = CSVDataManager()
    
    # リスト形式データを保存
    list_output_path = easy_dir / "game_scores_list.csv"
    csv_manager.save_to_csv(list_data, str(list_output_path))
    
    # 辞書形式データを保存  
    dict_output_path = easy_dir / "game_scores_dict.csv"
    csv_manager.save_dict_to_csv(dict_data, str(dict_output_path))
    
    # データを読み込んで確認
    loaded_list = csv_manager.load_from_csv(str(list_output_path))
    loaded_dict = csv_manager.load_dict_from_csv(str(dict_output_path))
    
    print(f"Easy - リストデータ読み込み結果: {len(loaded_list)}行")
    print(f"Easy - 辞書データ読み込み結果: {len(loaded_dict)}行")
    
    return str(list_output_path), str(dict_output_path)


def process_with_normal(list_data, dict_data, output_dir):
    """Normalレベル: pandasを使用したデータ処理"""
    print("\n=== Normal Level (Pandas) ===")
    
    # 出力ディレクトリを作成
    normal_dir = Path(output_dir) / "normal"
    normal_dir.mkdir(parents=True, exist_ok=True)
    
    # PandasCSVDataManagerを初期化
    data_manager = PandasCSVDataManager(str(normal_dir))
    
    # リスト形式データを保存（ヘッダーを除いたデータ部分のみ）
    columns = list_data[0]  # ヘッダー
    data_rows = list_data[1:]  # データ部分
    list_output_path = data_manager.save_array_list_to_csv(
        data_rows, "game_scores_list", columns
    )
    
    # 辞書形式データを保存
    dict_output_path = data_manager.save_dict_list_to_csv(
        dict_data, "game_scores_dict"
    )
    
    # データを読み込んで確認
    loaded_df_list = data_manager.load_csv("game_scores_list")
    loaded_df_dict = data_manager.load_csv("game_scores_dict")
    
    print(f"Normal - リストデータ読み込み結果: {len(loaded_df_list)}行")
    print(f"Normal - 辞書データ読み込み結果: {len(loaded_df_dict)}行")
    
    return list_output_path, dict_output_path


def process_with_hard(list_data, dict_data, output_dir):
    """Hardレベル: polarsを使用したデータ処理"""
    print("\n=== Hard Level (Polars) ===")
    
    # 出力ディレクトリを作成
    hard_dir = Path(output_dir) / "hard"
    hard_dir.mkdir(parents=True, exist_ok=True)
    
    # PolarsCSVDataManagerを初期化
    data_saver = PolarsCSVDataManager(str(hard_dir))
    
    # リスト形式データを保存（ヘッダーを除いたデータ部分のみ）
    columns = list_data[0]  # ヘッダー
    data_rows = list_data[1:]  # データ部分
    data_saver.save_array_data(data_rows, columns, "game_scores_list")
    
    # 辞書形式データをpolars形式に変換して保存
    # 辞書のリストを列指向の辞書に変換
    polars_dict = {}
    for key in dict_data[0].keys():
        polars_dict[key] = [row[key] for row in dict_data]
    
    data_saver.save_dict_data(polars_dict, "game_scores_dict")
    
    # データを読み込んで確認
    loaded_df_list = data_saver.read_csv("game_scores_list")
    loaded_df_dict = data_saver.read_csv("game_scores_dict")
    
    print(f"Hard - リストデータ読み込み結果: {len(loaded_df_list) if loaded_df_list is not None else 0}行")
    print(f"Hard - 辞書データ読み込み結果: {len(loaded_df_dict) if loaded_df_dict is not None else 0}行")
    
    list_path = Path(hard_dir) / "game_scores_list.csv"
    dict_path = Path(hard_dir) / "game_scores_dict.csv"
    return str(list_path), str(dict_path)


def main():
    """メイン処理"""
    print("Gaming Data Processing - Easy/Normal/Hard レベル比較")
    print("=" * 60)
    
    # 出力ディレクトリを設定
    output_dir = "/app/data"
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # サンプルデータを生成
    list_data, dict_data = create_sample_data()
    print(f"サンプルデータを生成しました: {len(list_data)-1}行のデータ")
    
    # 各レベルでデータ処理を実行
    try:
        # Easy レベル
        easy_list_path, easy_dict_path = process_with_easy(list_data, dict_data, output_dir)
        
        # Normal レベル  
        normal_list_path, normal_dict_path = process_with_normal(list_data, dict_data, output_dir)
        
        # Hard レベル
        hard_list_path, hard_dict_path = process_with_hard(list_data, dict_data, output_dir)
        
        # 結果サマリー
        print("\n" + "=" * 60)
        print("処理完了サマリー:")
        print("=" * 60)
        print("Easy Level 出力ファイル:")
        print(f"  - リスト形式: {easy_list_path}")
        print(f"  - 辞書形式: {easy_dict_path}")
        print("\nNormal Level 出力ファイル:")
        print(f"  - リスト形式: {normal_list_path}")
        print(f"  - 辞書形式: {normal_dict_path}")
        print("\nHard Level 出力ファイル:")
        print(f"  - リスト形式: {hard_list_path}")
        print(f"  - 辞書形式: {hard_dict_path}")
        
        # ファイルサイズ比較
        print("\n" + "=" * 60)
        print("ファイルサイズ比較:")
        print("=" * 60)
        
        def get_file_size(path):
            if os.path.exists(path):
                return os.path.getsize(path)
            return 0
        
        for data_type, paths in [
            ("リスト形式", [easy_list_path, normal_list_path, hard_list_path]),
            ("辞書形式", [easy_dict_path, normal_dict_path, hard_dict_path])
        ]:
            print(f"\n{data_type}:")
            for level, path in zip(["Easy", "Normal", "Hard"], paths):
                size = get_file_size(path)
                print(f"  {level:6}: {size:4} bytes - {path}")
                
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
