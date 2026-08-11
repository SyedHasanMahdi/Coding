import React, { useEffect, useState } from 'react';
import { StyleSheet, View, ActivityIndicator } from 'react-native';
import { WebView } from 'react-native-webview';
import { Asset } from 'expo-asset';
import * as FileSystem from 'expo-file-system';
import { StatusBar } from 'expo-status-bar';

export default function App() {
  const [htmlUri, setHtmlUri] = useState(null);

  useEffect(() => {
    (async () => {
      try {
        // Load the bundled HTML asset
        const asset = Asset.fromModule(require('./assets/tutor.html'));
        await asset.downloadAsync();

        // Copy it into a writable directory so WKWebView treats it as a
        // stable local file (helps with localStorage persistence)
        const destPath = FileSystem.documentDirectory + 'tutor.html';
        await FileSystem.copyAsync({
          from: asset.localUri,
          to: destPath,
        });

        setHtmlUri(destPath);
      } catch (e) {
        console.error('Failed to load tutor.html', e);
      }
    })();
  }, []);

  if (!htmlUri) {
    return (
      <View style={styles.center}>
        <ActivityIndicator size="large" />
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <StatusBar style="auto" />
      <WebView
        source={{ uri: htmlUri }}
        originWhitelist={['*']}
        javaScriptEnabled={true}
        domStorageEnabled={true}
        allowFileAccess={true}
        allowUniversalAccessFromFileURLs={true}
        mixedContentMode="always"
        startInLoadingState={true}
        style={styles.webview}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  webview: { flex: 1 },
  center: { flex: 1, justifyContent: 'center', alignItems: 'center' },
});