import React, { Component } from 'react'
import { View, Text, TouchableOpacity, TextInput, StyleSheet } from 'react-native'

class Inputs extends Component {
   state = {
      predictorUrl: '',
      captureFrequency: ''
   }
   handlePredictorUrl = (text) => {
      this.setState({ predictorUrl: text })
   }
   handleCaptureFrequence = (text) => {
      this.setState({ captureFrequency: text })
   }
   saveSettings = (predictorUrl, captureFrequency) => {
      alert('predictorUrl: ' + predictorUrl + ' captureFrequency: ' + captureFrequency)
   }
   render() {
      return (
         <View style = {styles.container}>
            <TextInput style = {styles.input}
               underlineColorAndroid = "transparent"
               placeholder = "Predictor URL"
               placeholderTextColor = "#9a73ef"
               autoCapitalize = "none"
               onChangeText = {this.handlePredictorUrl}/>
            
            <TextInput style = {styles.input}
               underlineColorAndroid = "transparent"
               placeholder = "Capture Frequency"
               placeholderTextColor = "#9a73ef"
               autoCapitalize = "none"
               onChangeText = {this.handleCaptureFrequency}/>
            
            <TouchableOpacity
               style = {styles.saveButton}
               onPress = {
                  () => this.saveSettings(this.state.predictorUrl, this.state.captureFrequency)
               }>
               <Text style = {styles.saveButtonText}> Save setttings </Text>
            </TouchableOpacity>
         </View>
      )
   }
}
export default Inputs

const styles = StyleSheet.create({
   container: {
      paddingTop: 23
   },
   input: {
      margin: 15,
      height: 40,
      borderColor: '#7a42f4',
      borderWidth: 1
   },
   saveButton: {
      backgroundColor: '#7a42f4',
      padding: 10,
      margin: 15,
      height: 40,
   },
   saveButtonText:{
      color: 'white'
   }
})