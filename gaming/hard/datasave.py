from pathlib import Path
from typing import Any, Dict, List, Union

import polars as pl


class CSVDataManager:
    """
    Polarsを使用して配列データと辞書型データをCSVファイルに保存するクラス
    """
    
    def __init__(self, base_dir: str = "/app/data"):
        """
        初期化
        
        Args:
            base_dir (str): 保存先のベースディレクトリ
        """
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)
    
    def save_array_data(self, data: List[List[Any]], columns: List[str], filename: str) -> bool:
        """
        配列データをCSVファイルに保存
        
        Args:
            data (List[List[Any]]): 2次元配列データ
            columns (List[str]): カラム名のリスト
            filename (str): 保存するファイル名（.csv拡張子は自動で追加）
        
        Returns:
            bool: 保存成功時True、失敗時False
        """
        try:
            # ファイル名に.csv拡張子を追加（まだない場合）
            if not filename.endswith('.csv'):
                filename += '.csv'
            
            # DataFrameを作成
            df = pl.DataFrame(data, schema=columns)
            
            # ファイルパスを構築
            filepath = self.base_dir / filename
            
            # CSVファイルに保存
            df.write_csv(filepath)
            
            print(f"配列データを保存しました: {filepath}")
            return True
            
        except Exception as e:
            print(f"配列データの保存に失敗しました: {e}")
            return False
    
    def save_dict_data(self, data: Dict[str, List[Any]], filename: str) -> bool:
        """
        辞書型データをCSVファイルに保存
        
        Args:
            data (Dict[str, List[Any]]): カラム名をキー、値のリストを値とする辞書
            filename (str): 保存するファイル名（.csv拡張子は自動で追加）
        
        Returns:
            bool: 保存成功時True、失敗時False
        """
        try:
            # ファイル名に.csv拡張子を追加（まだない場合）
            if not filename.endswith('.csv'):
                filename += '.csv'
            
            # DataFrameを作成
            df = pl.DataFrame(data)
            
            # ファイルパスを構築
            filepath = self.base_dir / filename
            
            # CSVファイルに保存
            df.write_csv(filepath)
            
            print(f"辞書データを保存しました: {filepath}")
            return True
            
        except Exception as e:
            print(f"辞書データの保存に失敗しました: {e}")
            return False
    
    def append_dict_data(self, data: Dict[str, List[Any]], filename: str) -> bool:
        """
        既存のCSVファイルに辞書型データを追加
        
        Args:
            data (Dict[str, List[Any]]): 追加するデータ
            filename (str): 対象ファイル名
        
        Returns:
            bool: 追加成功時True、失敗時False
        """
        try:
            if not filename.endswith('.csv'):
                filename += '.csv'
            
            filepath = self.base_dir / filename
            
            # 新しいデータフレームを作成
            new_df = pl.DataFrame(data)
            
            # 既存ファイルがある場合は読み込んで結合
            if filepath.exists():
                existing_df = pl.read_csv(filepath)
                combined_df = pl.concat([existing_df, new_df])
            else:
                combined_df = new_df
            
            # CSVファイルに保存
            combined_df.write_csv(filepath)
            
            print(f"データを追加しました: {filepath}")
            return True
            
        except Exception as e:
            print(f"データの追加に失敗しました: {e}")
            return False
    
    def list_saved_files(self) -> List[str]:
        """
        保存されているCSVファイルの一覧を取得
        
        Returns:
            List[str]: CSVファイル名のリスト
        """
        csv_files = [f.name for f in self.base_dir.glob("*.csv")]
        return sorted(csv_files)
    
    def read_csv(self, filename: str) -> Union[pl.DataFrame, None]:
        """
        保存されたCSVファイルを読み込み
        
        Args:
            filename (str): 読み込むファイル名
        
        Returns:
            Union[pl.DataFrame, None]: データフレーム、失敗時はNone
        """
        try:
            if not filename.endswith('.csv'):
                filename += '.csv'
            
            filepath = self.base_dir / filename
            
            if not filepath.exists():
                print(f"ファイルが見つかりません: {filepath}")
                return None
            
            df = pl.read_csv(filepath)
            return df
            
        except Exception as e:
            print(f"ファイルの読み込みに失敗しました: {e}")
            return None
