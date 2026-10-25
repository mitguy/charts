package main

import (
	"math"
	"time"

	"charts/jira"

	"github.com/goforj/godump"
	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
)

func main() {
	issues := jira.FetchAll("project = Kafka and Status = Closed and created >= startOfMonth(-12)")

	// godump.Dump(issues)

	godump.Dump(len(issues))

	// var data []float64

	// for _, issue := range issues {
	// 	data = append(data, time.Time(issue.Fields.Resolutiondate).Sub(time.Time(issue.Fields.Created)).Hours()/24)
	// }

	// for _, item := range data {
	// 	fmt.Println(item)
	// }

	plotterValues := make(plotter.Values, len(issues))

	for i, issue := range issues {
		plotterValues[i] = time.Time(issue.Fields.Resolutiondate).Sub(time.Time(issue.Fields.Created)).Hours()
	}

	godump.Dump(plotterValues)

	// p75, _ := stats.Percentile(data, 75)
	// p25, _ := stats.Percentile(data, 25)

	// FreedmanDiaconis := int(2 * ((p75 - p25) / math.Cbrt(math.Pi)))
	Sturges := int(math.Ceil(math.Log2(float64(len(issues))) + 1))

	hist, err := plotter.NewHist(plotterValues, Sturges)
	if err != nil {
		panic(err)
	}

	p := plot.New()

	p.Title.Text = "1. Time/Tasks Distribution"
	p.X.Label.Text = "Time Spent (Days)"
	p.Y.Label.Text = "Amount of Tasks"

	// bins := make([]plotter.HistogramBin, 0)
	//
	// for lo := 0.0; lo < 50; lo += 5 {
	// 	bins = append(bins, plotter.HistogramBin{Min: lo, Max: lo + 5, Weight: 0})
	// }
	//
	// for _, v := range plotterValues {
	// 	idx := int(v / 5)
	// 	if idx >= 0 && idx < len(bins) {
	// 		bins[idx].Weight++
	// 	}
	// }
	//
	// hist := &plotter.Histogram{Bins: bins, Width: 1, FillColor: color.Gray{200}, LineStyle: plotter.DefaultLineStyle}

	// hist.Color = color.RGBA{R: 50, G: 120, B: 220, A: 255}
	p.Add(hist)

	if err := p.Save(512, 512, "histogram.png"); err != nil {
		panic(err)
	}
}
