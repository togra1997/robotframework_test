import os
from typing import Any, Dict, List

import pandas as pd


class CSVDataManager:
    """データをCSV形式で保存するためのクラス"""
    
    def __init__(self, base_path: str = "/app/data"):
        """
        初期化
        
        Args:
            base_path: CSVファイルを保存するベースパス
        """
        self.base_path = base_path
        os.makedirs(base_path, exist_ok=True)
    
    def save_dict_to_csv(self, data: Dict[str, Any], filename: str) -> str:
        """
        辞書型データをCSVファイルに保存
        
        Args:
            data: 保存する辞書データ
            filename: ファイル名（.csv拡張子は自動付与）
        
        Returns:
            保存されたファイルのパス
        """
        if not filename.endswith('.csv'):
            filename += '.csv'
        
        filepath = os.path.join(self.base_path, filename)
        
        # 辞書をDataFrameに変換
        df = pd.DataFrame([data])
        df.to_csv(filepath, index=False, encoding='utf-8')
        
        return filepath
    
    def save_dataframe_to_csv(self, df: pd.DataFrame, filename: str) -> str:
        """
        DataFrameを直接CSVファイルに保存
        
        Args:
            df: 保存するDataFrame
            filename: ファイル名（.csv拡張子は自動付与）
        
        Returns:
            保存されたファイルのパス
        """
        if not filename.endswith('.csv'):
            filename += '.csv'
        
        filepath = os.path.join(self.base_path, filename)
        df.to_csv(filepath, index=False, encoding='utf-8')
        
        return filepath
    
    def load_csv(self, filename: str) -> pd.DataFrame:
        """
        CSVファイルを読み込んでDataFrameとして返す
        
        Args:
            filename: ファイル名
        
        Returns:
            読み込んだDataFrame
        """
        if not filename.endswith('.csv'):
            filename += '.csv'
        
        filepath = os.path.join(self.base_path, filename)
        return pd.read_csv(filepath, encoding='utf-8')
    
    def save_dict_list_to_csv(self, data: List[Dict[str, Any]], filename: str) -> str:
        """
        辞書のリストをCSVファイルに保存
        
        Args:
            data: 保存する辞書のリスト
            filename: ファイル名（.csv拡張子は自動付与）
        
        Returns:
            保存されたファイルのパス
        """
        if not filename.endswith('.csv'):
            filename += '.csv'
        
        filepath = os.path.join(self.base_path, filename)
        
        # 辞書のリストをDataFrameに変換
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False, encoding='utf-8', header=False)
        
        return filepath
    
    def save_array_list_to_csv(self, data: List[List], filename: str, columns: List[str] = None) -> str:
        """
        配列のリストをCSVファイルに保存
        
        Args:
            data: 保存する配列のリスト
            filename: ファイル名（.csv拡張子は自動付与）
            columns: カラム名のリスト
        
        Returns:
            保存されたファイルのパス
        """
        if not filename.endswith('.csv'):
            filename += '.csv'
        
        filepath = os.path.join(self.base_path, filename)
        
        # 配列のリストをDataFrameに変換
        df = pd.DataFrame(data, columns=columns)
        df.to_csv(filepath, index=False, encoding='utf-8')
        
        return filepath
