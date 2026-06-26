import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt

# 列名与数据对其显示
# pd.set_option('display.unicode.ambiguous_as_wide', True)
# pd.set_option('display.unicode.east_asian_width', True)
# # 显示所有列
# pd.set_option('display.max_columns', None)
# # 显示所有行
# pd.set_option('display.max_rows', None)

fund_info_index_em_df = ak.fund_info_index_em(symbol="行业主题", indicator="增强指数型")
print(fund_info_index_em_df)


# fund_portfolio_industry_allocation_em_df = ak.fund_portfolio_industry_allocation_em(symbol="014419", date="2026")
# print(fund_portfolio_industry_allocation_em_df)

# fund_portfolio_change_em_df1 = ak.fund_portfolio_change_em(symbol="014419", indicator="累计买入", date="2026")
# print(fund_portfolio_change_em_df1)
# fund_portfolio_change_em_df2 = ak.fund_portfolio_change_em(symbol="014419", indicator="累计卖出", date="2026")
# print(fund_portfolio_change_em_df2)

# stock_report_fund_hold_detail_df = ak.stock_report_fund_hold_detail(symbol="005827", date="2026-03-31")
# print(stock_report_fund_hold_detail_df)

# 同花顺-板块-行业板块-指数日频率数据
stock_board_industry_name_em_df = ak.stock_board_industry_name_em()
print(stock_board_industry_name_em_df)

# stock_industry_sina_df = ak.stock_sector_spot(indicator="新浪行业")
# print(stock_industry_sina_df)