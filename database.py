from sqlalchemy import create_engine, text

#engine = create_engine("mysql+pymysql://root:FFD5hhBe4BdC4cBgGfdCbCD--2D3fFDc@viaduct.proxy.rlwy.net/railway?charset=utf8mb4")
engine = create_engine("mysql+pymysql://root:FFD5hhBe4BdC4cBgGfdCbCD--2D3fFDc@viaduct.proxy.rlwy.net/railway", pool_pre_ping=True)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM record"))
    for row in result:
        print(row)