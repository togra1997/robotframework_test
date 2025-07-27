import csv
import os


class CSVDataManager:
    """CSVファイルのデータ保存・読み込みを管理するクラス"""
    
    def __init__(self, default_encoding='utf-8'):
        """
        初期化
        
        Args:
            default_encoding: デフォルトの文字エンコーディング
        """
        self.default_encoding = default_encoding
    
    def save_to_csv(self, data, filename):
        """
        データをCSVファイルに保存する
        
        Args:
            data: 保存するデータ（リストのリスト形式）
            filename: 保存先のファイル名
        """
        with open(filename, 'w', newline='', encoding=self.default_encoding) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
        print(f"データを {filename} に保存しました。")

    def load_from_csv(self, filename):
        """
        CSVファイルからデータを読み込む
        
        Args:
            filename: 読み込むファイル名
            
        Returns:
            読み込んだデータ（リストのリスト形式）
        """
        if not os.path.exists(filename):
            print(f"ファイル {filename} が見つかりません。")
            return []
        
        data = []
        with open(filename, 'r', newline='', encoding=self.default_encoding) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        print(f"{filename} からデータを読み込みました。")
        return data

    def save_dict_to_csv(self, data, filename):
        """
        辞書形式のデータをCSVファイルに保存する
        
        Args:
            data: 保存するデータ（辞書のリスト形式）
            filename: 保存先のファイル名
        """
        if not data:
            print("保存するデータがありません。")
            return
        
        fieldnames = data[0].keys()
        with open(filename, 'w', newline='', encoding=self.default_encoding) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"辞書データを {filename} に保存しました。")

    def load_dict_from_csv(self, filename):
        """
        CSVファイルから辞書形式でデータを読み込む
        
        Args:
            filename: 読み込むファイル名
            
        Returns:
            読み込んだデータ（辞書のリスト形式）
        """
        if not os.path.exists(filename):
            print(f"ファイル {filename} が見つかりません。")
            return []
        
        data = []
        with open(filename, 'r', newline='', encoding=self.default_encoding) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
        print(f"{filename} から辞書データを読み込みました。")
        return data
    
    def append_to_csv(self, data, filename):
        """
        既存のCSVファイルにデータを追加する
        
        Args:
            data: 追加するデータ（リストのリスト形式）
            filename: 追加先のファイル名
        """
        with open(filename, 'a', newline='', encoding=self.default_encoding) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
        print(f"データを {filename} に追加しました。")
    
    def file_exists(self, filename):
        """
        ファイルが存在するかチェック
        
        Args:
            filename: チェックするファイル名
            
        Returns:
            ファイルが存在する場合True、しない場合False
        """
        return os.path.exists(filename)
