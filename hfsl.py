def hfsl(csv_file, savefig_file):
    import csv
    data = []
    with open(csv_file) as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    x=[]
    y=[]
    z = []
    for row in data[3:]:
        x.append(int(row[0]))
        y.append(int(row[1].replace(',', '')))
        z.append(int(row[2].replace(',', '')))


    import matplotlib.pyplot as plt
    plt.figure()

    ax1 = plt.gca()
    ax1.set_xlim([0,110])
    ax1.set_ylim([0,max(y)*1.1])
    ax1.plot(x,y)
    # ax1.axvline(max(x),zorder =0, linestyle='--')
    # ax1.axhline(max(y),zorder =0)

    ax2 = ax1.twinx()
    ax2.bar(x,z,color = "orange")
    ax2.set_ylim([0,2*max(z)])

    ax1.set_zorder(2.5)
    ax1.set_frame_on(False)

    w = [j/i for i,j in zip(y,z)]
    ax3 = ax2.twinx()
    ax3.set_ylim([0,0.1])
    ax3.bar(x,w,color='red',alpha = 0.4)

    u = [j/i for i,j in zip(x,y)]
    ax4 = ax3.twinx()
    ax4.set_ylim([0,2*max(z)])
    # ax4.plot(x,u,color = 'green')

    # Hide the y-axis numbers (tick labels) for ax3
    ax1.tick_params(axis = 'y', labelright = False, labelleft = True,right=False, left=True,
                    colors = '#1f77b4')
    ax2.tick_params(axis = 'y', labelright = True, labelleft = False,right=True, left=False,
                    colors = 'orange')

    from matplotlib.ticker import PercentFormatter
    ax3.yaxis.set_major_formatter(PercentFormatter(xmax=1.0))
    ax3.tick_params(axis='y', right=True, left = False, labelright=True, labelleft=False, 
                    colors = 'red')
    ax3.spines['right'].set_position(('outward', 60))

    ax4.tick_params(axis='y', right=False, left = False, labelright=False, labelleft=False)
    ax4.spines['left'].set_position(('outward', 60))

    
    
    plt.tight_layout()

    plt.savefig(savefig_file,dpi = 200)
    # plt.clf()

if __name__ == "__main__":
    hfsl('hp.csv', 'hp.png')
    hfsl('fp.csv', 'fp.png')
