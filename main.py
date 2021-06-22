import network

net = network.WaterDistributionNetwork("ctown_pd.inp")
net.set_time_params(duration=3600, hydraulic_step=300)
net.run()

print(net.df_nodes_report)