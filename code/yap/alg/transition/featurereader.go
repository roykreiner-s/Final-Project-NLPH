package transition

import (
	"io/ioutil"

	"github.com/go-yaml/yaml"
	// "log"
)

type FeatureGroup struct {
	Group      string
	Transition string
	Features   []string
	Idle       bool
	Associated bool
}

type MorphTemplate struct {
	Group        string
	Combinations []string
}
type FeatureSetup struct {
	FeatureGroups  []FeatureGroup  `yaml:"feature groups"`
	MorphTemplates []MorphTemplate `yaml:"morph templates"`
}

func (s *FeatureSetup) NumFeatures() int {
	var (
		numFeatures int
		groupId     int
		exists      bool
	)
	groupMap := make(map[string]int)

	for i, group := range s.FeatureGroups {
		numFeatures += len(group.Features)
		groupMap[group.Group] = i
	}

	for _, tmpl := range s.MorphTemplates {
		groupId, exists = groupMap[tmpl.Group]
		if exists {
			numFeatures += len(s.FeatureGroups[groupId].Features) * len(tmpl.Combinations)
		}
	}
	return numFeatures
}

func LoadFeatureConf(conf []byte) *FeatureSetup {
	setup := new(FeatureSetup)
	yaml.Unmarshal(conf, setup)
	return setup
}

func LoadFeatureConfFile(filename string) (*FeatureSetup, error) {
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		return nil, err
	}
	setup := LoadFeatureConf(data)
	return setup, nil
}
